import requests
import argparse
#Importing exceptions module
from requests.exceptions import RequestException

#Function for fetching headers
def fetch_headers(url):
    try:
        req = requests.get(url, timeout=(4,10))
        return req.status_code, req.headers, None
    except RequestException as e:
        return None, None, str(e)

#Function for Analysing Headers
def analyse_headers(headers):
    headers_dictionary = {
        "Strict-Transport-Security" : "Protects against MitM",
        "Content-Security-Policy" : "Protects against XSS(Cross-Site Scripting)",
        "X-Content-Type-Options" : "Protects against MIME-type sniffing",
        "X-Frame-Options" : "Protects against clickjacking"
    }
    result = {}
    for header, description in headers_dictionary.items():
        result[header] = header in headers
    return result
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= "HTTP Security Inspector tool")
    parser.add_argument("url", help = "Target URL to inspect")
    args = parser.parse_args()
    target = args.url
    print(f"Target: {target}\n")

    status_code, headers, error = fetch_headers(target)

    if error:
        print(f"[-] Request Failed: {error}")
    else:
        print(f"[+] Status Code: {status_code}\n")

        analysis_result = analyse_headers(headers)

        for header, is_present in analysis_result.items():
            if is_present:
                print(f"[FOUND] {header}")
            else:
                print(f"[MISSING] {header}")



