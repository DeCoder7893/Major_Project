import nmap
import sys
# take the range of ports to
# be scanned
ports = [21,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]


# assign the target ip to be scanned to
# a variable
target = '199.79.62.128'

# instantiate a PortScanner object
scanner = nmap.PortScanner()

for i in ports:

	# scan the target port
	res = scanner.scan(target,str(i))

	# the result is a dictionary containing
	# several information we only need to
	# check if the port is opened or closed
	# so we will access only that information
	# in the dictionary
	res = res['scan'][target]['tcp'][i]['state']

	print(f'port {i} is {res}.')
