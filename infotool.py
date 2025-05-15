
import sys
import socket
import requests
import json

def get_ip_address(website_url):
    try:
        ip = socket.gethostbyname(website_url)
        return ip
    except socket.gaierror:
        print("Error: Unable to resolve domain.")
        sys.exit(1)

def get_location_info(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            return response.json()
        else:
            print("Error: Unable to retrieve data from ipinfo.io")
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python infotool.py <websiteurl>")
        sys.exit(1)

    website_url = sys.argv[1]
    print(f"\n[+] Getting IP address for: {website_url}")
    ip = get_ip_address(website_url)
    print(f"[+] IP Address: {ip}")

    print("\n[+] Fetching location information...")
    location_info = get_location_info(ip)

    print("\n[+] Location Information (JSON):")
    print(json.dumps(location_info, indent=4))

if __name__ == "__main__":
    main()
