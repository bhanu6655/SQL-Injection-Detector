from colorama import init, Fore
import requests
from requests.exceptions import RequestException

init(autoreset=True)

def is_vulnerable(response):
    errors = {
        "mysql": [
            "you have an error in your sql syntax",
            "warning: mysql"
        ],
        "sql_server": [
            "unclosed quotation mark",
            "incorrect syntax near"
        ],
        "oracle": [
            "quoted string not properly terminated",
            "ora-00933",
            "ora-00936"
        ],
        "postgresql": [
            "pg_query",
            "syntax error at or near"
        ]
    }

    content = response.text.lower()

    for db, error_list in errors.items():
        for error in error_list:
            if error in content:
                print(Fore.GREEN + f"[!] SQL Injection detected: {error} ({db})")
                return True
    return False


def scan(url):
    payloads = [
        "'", "' OR 1=1--", "' OR '1'='1"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print(Fore.YELLOW + f"[+] Scanning: {url}")

    try:
        baseline = requests.get(url, headers=headers, timeout=5)
        base_len = len(baseline.text)

        for payload in payloads:
            test_url = url + payload
            try:
                res = requests.get(test_url, headers=headers, timeout=5)

                if abs(len(res.text) - base_len) > 50:
                    print(Fore.YELLOW + f"[!] Possible change with payload: {payload}")

                if is_vulnerable(res):
                    print(Fore.GREEN + f"[+] Vulnerable with payload: {payload}")
                else:
                    print(Fore.RED + f"[-] Not vulnerable: {payload}")

            except RequestException as e:
                print(Fore.RED + f"[!] Error: {e}")

    except RequestException as e:
        print(Fore.RED + f"[!] Failed to connect: {e}")


if __name__ == "__main__":
    url = input("Enter URL (e.g., http://example.com?id=): ")
    scan(url)
