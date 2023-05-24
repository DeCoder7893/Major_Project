import socket
import sys

host = sys.argv[1]
ports = [21,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        print(f"Port {port} is open")
        s.close()
    except:
        pass

for port in ports:
    scan_port(port)