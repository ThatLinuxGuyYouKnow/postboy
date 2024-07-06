import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Find endpoints on a target URL using a wordlist.")
    parser.add_argument('-t', '--target', required=True, help='Target URL (e.g., http://example.com)')
    parser.add_argument('-d', '--dictionary', required=True, help='Path to the wordlist file')
    args = parser.parse_args()

    url = args.target.rstrip('/') + "/{}"
    wordlist_file = args.dictionary
    output_file = "found_endpoints.out"

    # Read wordlist from file
    with open(wordlist_file, 'r') as file:
        endpoints = file.read().splitlines()

    # Open output file in write mode
    with open(output_file, 'w') as output:
        for endpoint in endpoints:
            full_url = url.format(endpoint)
            
            # Test GET request
            try:
                response_get = requests.get(full_url)
                print(f"GET {full_url}: {response_get.status_code}")
                if response_get.status_code != 404:
                    output.write(f"GET {full_url}: {response_get.status_code}\n")
            except requests.RequestException as e:
                print(f"Error GET {full_url}: {e}")

            # Test POST request
            try:
                response_post = requests.post(full_url)
                print(f"POST {full_url}: {response_post.status_code}")
                if response_post.status_code != 404:
                    output.write(f"POST {full_url}: {response_post.status_code}\n")
            except requests.RequestException as e:
                print(f"Error POST {full_url}: {e}")

if __name__ == "__main__":
    main()
