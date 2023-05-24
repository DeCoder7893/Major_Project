import requests
from bs4 import BeautifulSoup
import whois
import dns.resolver
import sys

print("\n|----------------Give domain name of website-----------------------|")
print("\n|                                                                  |")
print("\n|                                                                  |")
print("\n|                                                                  |")
print("\n|------------------------------------------------------------------|")

target = sys.argv[1]
# Retrieve website's HTML content
response = requests.get("http://" + target)
html_content = response.text

# Extract metadata
soup = BeautifulSoup(html_content, "html.parser")
title = soup.title.string

# Perform DNS lookup
dns_records = dns.resolver.resolve(target, "A")
ip_addresses = [record.address for record in dns_records]

# Fetch WHOIS information
domain_info = whois.whois(target)
registrant = domain_info.registrant_name
creation_date = domain_info.creation_date
expiration_date = domain_info.expiration_date

# Identify subdomains
subdomains = []
for subdomain in ["www", "mail", "ftp"]:
    subdomain_target = subdomain + "." + target
    try:
        subdomain_response = requests.get("http://" + subdomain_target)
        if subdomain_response.status_code == 200:
            subdomains.append(subdomain_target)
    except requests.exceptions.RequestException:
        pass

# Print gathered information
print("Website: {}".format(target))
print("Title: {}".format(title))
print("IP addresses: {}".format(ip_addresses))
print("Registrant: {}".format(registrant))
print("Creation date: {}".format(creation_date))
print("Expiration date: {}".format(expiration_date))
print("Subdomains: {}".format(subdomains))
