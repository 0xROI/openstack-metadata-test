import requests
import os

METADATA_BASE = "http://169.254.169.254/openstack/latest/"
ENDPOINTS = [
    "meta_data.json",
    "user_data",
    "network_data.json",
    "vendor_data.json",
    "vendor_data2.json",
    "context.json"
]

OUTPUT_DIR = "metadata_output"

def save_to_file(filename, content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def test_metadata_service():
    print("[*] Testing access to OpenStack metadata service...\n")
    for endpoint in ENDPOINTS:
        url = METADATA_BASE + endpoint
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] {endpoint} accessible, saving to file...")
                content = response.text.strip()
                print(f"{'-'*60}")
                print(content)
                print(f"{'-'*60}\n")
                save_to_file(endpoint.replace("/", "_"), content)
            else:
                print(f"[-] {endpoint} returned status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error accessing {url}: {e}")

if __name__ == "__main__":
    test_metadata_service()
