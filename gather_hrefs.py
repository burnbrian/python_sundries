import requests
import re
from colorama import Fore
from urllib.parse import urlparse

def gather_hrefs(url):
    gathered_hrefs = {}
    try:
        response = requests.get(url)
        if response.status_code == 200:
            hrefs = re.findall(r'(?i)href=[\'"]?([^\'" >]+)', response.text)
            for href in hrefs:
                if href.lower().startswith("http") or href.lower().startswith("https"):
                    gathered_hrefs[href] = href
                elif href.startswith("/"):
                    gathered_hrefs[href] = url + href
                else:
                    print(f"{Fore.RED}URL: {href} may be external or not a valid URL.")
    except Exception as e:
        print(f"Error: {e}")
    return gathered_hrefs

def main():
    # Add definition to make recursive calls to gather_hrefs
    url = "http://www.sans.org"
    gathered_hrefs = gather_hrefs(url)
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    for i in gathered_hrefs:
        if domain in gathered_hrefs[i]:
            print(f"{Fore.GREEN}URL: {gathered_hrefs[i]}")

if __name__ == "__main__":
    main()