import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Find endpoints on a target URL using a wordlist.")
    parser.add_argument('-t', '--target', required=True, help='Target URL (e.g., http://example.com)')
    parser.add_argument('-d', '--dictionary', required=True, help='Path to the wordlist file')
    args = parser.parse_args()

    url = args.target + "/{}"
    wordlist_file = args.dictionary
    output_file = "found_endpoints.txt"

    # Read wordlist from file
    with open(wordlist_file, 'r') as file:
        endpoints = file.read().splitlines()

    # Open output file in write mode
    with open(output_file, 'w') as output:
        for endpoint in endpoints:
            full_url = url.format(endpoint)
            try:
                response = requests.post(full_url)
                print(f"Testing {full_url}: {response.status_code}")
                if response.status_code != 404:
                    output.write(f"Found {full_url}: {response.status_code}\n")
                    print(f"Found {full_url}: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error testing {full_url}: {e}")

if __name__ == "__main__":
    main()
