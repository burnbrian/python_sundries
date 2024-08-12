import re
import pathlib

def get_log_ips(log_path_dir):
    """Return a list of IP addresses from DNS logs in a directory."""
    """Example: '/home/student/Public/log/dnslogs'"""
    log_ips = []
    dir_list = pathlib.Path(log_path_dir)
    for log in dir_list.rglob("*"):
        if not log.is_file():
            continue
        else:
            with log.open() as f:
                log_text = f.read()
                ipv4_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
                for ip in re.findall(ipv4_regex, log_text):
                    log_ips.append(ip)
    return log_ips

def main():
    try:
        """Hard coded path for testing"""
        log_path_dir = '/home/student/Public/log/dnslogs'
        print(get_log_ips(log_path_dir))
    except:
        pass

if __name__ == "__main__":
    main()