import requests

def get_ip():
    url = "https://httpbin.org/ip"

    try:
        response = requests.get(url, timeout =(3, 10))
        response.raise_for_status()

        data = response.json()
        ip_address = data.get("origin")
        if not ip_address:
            print("[-] Error: 'orgin' key missing from response data")
            return None

        print(f"[+] Success! My Public IP is: {ip_address}")
        return ip_address

    except requests.exceptions.Timeout:
        print("[-] Error: The request timed out.")
    except requests.exceptions.HTTPError as http_error:
        print(f"[-] HTTP Error occurred: {http_error}")
    except requests.exceptions.RequestException as error:
        print(f"[-] A network error occurred: {error}")

if __name__ == "__main__":
    get_ip()


