# Configure container
FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
ADD sites-enabled/app /etc/nginx/conf.d/default.conf

# Add the SweetBiz SSL certificate and key to the container
COPY --chown=nginx:nginx cert.pem /etc/nginx/cert.pem
COPY --chown=nginx:nginx key.pem /etc/nginx/key.pem