import requests
import re

url = input("Enter the URL to scan: ")
response = requests.get(url)
page_content = response.content.decode("utf-8")

# Find links on the page
links = re.findall('"((http|ftp)s?://.*?)"', page_content)

for link in links:
    try:
        link_response = requests.get(link[0])
        if link_response.status_code == 404:
            print(f"404 Not Found: {link[0]}")
        elif "password" in link_response.content.decode("utf-8").lower():
            print(f"Password field found: {link[0]}")
        elif "sql" in link_response.content.decode("utf-8").lower():
            print(f"SQL injection possible: {link[0]}")
        elif "xss" in link_response.content.decode("utf-8").lower():
            print(f"Cross-site scripting possible: {link[0]}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
