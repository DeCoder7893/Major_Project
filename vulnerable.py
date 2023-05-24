import requests
import sys
import time
import nmap
from zapv2 import ZAPv2
from bs4 import BeautifulSoup

target    = sys.argv[1]
nmap_args   = "-sV -O"
zap_api_key = "u2gpootapp0be1q1k52pd557jr"

# Start the OWASP ZAP API
zap = ZAPv2(apikey="u2gpootapp0be1q1k52pd557jr")

# Launch the browser and visit the target website
print("Accessing target...")
zap.urlopen(target)
time.sleep(2)

# Spider the website to find all links and pages
print("Spidering target...")
zap.spider.scan(target)
time.sleep(2)
while (int(zap.spider.status) < 100):
    print("Spider progress %: " + zap.spider.status)
    time.sleep(2)
print("Spider complete.")

# Perform an active scan to find vulnerabilities
print("Scanning target...")
zap.ascan.scan(target)
while (int(zap.ascan.status) < 100):
    print("Scan progress %: " + zap.ascan.status)
    time.sleep(2)
print("Scan complete.")

# Use Nmap to perform a port scan and OS detection
print("Performing Nmap scan...")
nm = nmap.PortScanner()
nm.scan(target, arguments=nmap_args)
open_ports = []
for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        for port in lport:
            open_ports.append(port)
print("Nmap scan complete.")

# Search for vulnerabilities in the HTML response
print("Searching for vulnerabilities in HTML response...")
response = requests.get(target)
html = response.content
soup = BeautifulSoup(html, "html.parser")
vulns = []
for tag in soup.find_all():
    for attr, value in tag.attrs.items():
        if "javascript:" in str(value).lower():
            vulns.append("JavaScript injection vulnerability found.")
print("HTML response scan complete.")

# Generate the report
print("Generating report...")
report = zap.core.htmlreport()
with open("report.html", "w") as f:
    f.write(report)
print("Report generated.")

# Display the results
print("Results:\n")
print("Open ports: {}".format(open_ports))
print("Vulnerabilities: {}".format(vulns))