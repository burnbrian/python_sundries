import os
import socket
from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from redis import Redis

app = Flask(__name__)

# Redis database
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

# Configuration
app.config.update(
    DEBUG = False,
    SECRET_KEY = 'SDJWDKFDJNVCMNVCSLKJDFLJKWOWDFOJCVN'
)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Mixing
class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

# Users
user1 = User(id=1, name="justinb", password="pass")
user2 = User(id=2, name="kevinp", password="pass")

# Home
@app.route('/')
@login_required
def home():
    return Response(f'''
                    <html>
                        <body>
                            <h1>Flags:</h1>
                            <ul>
                                <li><a href="/flag1">Course practical...</a></li>
                                <li><a href="/flag2">Capture the flag...</a></li>
                                <li><a href="/logout">Logout...</a></li>
                            </ul>
                         </body>
                    </html>
                    ''')

# Route back to this if not logged in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Is user 1?
        if username == user1.name and password == user1.password:
            login_user(user1)
            return redirect(request.args.get("next") or url_for("flag2"))
        # Is user 2?
        elif username == user2.name and password == user2.password:
            login_user(user2)
            return redirect(request.args.get("next") or url_for("flag1"))
        # Is nobody?
        else:
            return abort(401)
    else:
        redis.incr('hits')
        hits = redis.get('hits').decode('utf-8')
        return Response(f'''
        <html>
            <body>
                <h1>Hello Hackers</h1>
                <p>I've been visited {hits} times.</p>
                <p>You probably want to login.</p>
                <p>You may be able to hack me, but there's probably a better way.</p>
                <form action="" method="post">
                    <p><input type=text name=username>
                    <p><input type=password name=password>
                    <p><input type=submit value=Login>
                </form>
            </body>
        </html>
        ''')

# Flag #1, only for kevinp
@app.route('/flag1')
@login_required
def flag1():
    if current_user.name == "kevinp":
        return Response(f'''
                        <html>
                            <body>
                                <h1>Flag: Flag #1</h1>
                            </body>
                        </html>
                        ''')
    else:
        abort(403)

# Flag #2, only for justinb
@app.route('/flag2')
@login_required
def flag2():
    if current_user.name == "justinb":
        return Response(f'''
                        <html>
                            <body>
                                <h1>Flag: Flag #2</h1>
                            </body>
                        </html>
                        ''')
    else:
        abort(403)

# Failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>', status=401)

# Logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

# Reload
@login_manager.user_loader
def load_user(user_id):
    if user_id == str(user1.id):
        return user1
    if user_id == str(user2.id):
        return user2
    return None

# Local testing only, not for production
# Forward through gunicorn + nginx
if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0', ssl_context="adhoc", port="8000", debug=False)