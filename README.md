Postboy

An opsec tool for endpoint discovery via POST requests. Postboy is a Python script that tests endpoints on a target URL using a wordlist. It sends HTTP POST requests to the endpoints and logs the results.

This tool exists because other endpoint discovery tools(like Gobuster) are only configured to send GETrequests, this causes false negatives as some endpoints are only configured for POST requests.
Requirements

    Python 3.x
    requests library

You can install the requests library using pip:

pip install requests

Usage

To use Postboy, you need to provide a target URL and a wordlist file. The wordlist file should contain a list of endpoints, one per line.
Command-Line Arguments

-t, --target: The target URL (e.g., http://example.com).
-d, --dictionary: The path to the wordlist file.

Example

python postboy.py -t http://super.evilcorpserver.com -d lists.txt

Output

The script will create an output file named found_endpoints.txt in the same directory, containing the endpoints that do not return a 404 status code.
Development Roadmap

    Make multithreaded to increase speed

    Configure to support GET requests

    Detect redirects( prevents false positives when this tool is used on websites )
