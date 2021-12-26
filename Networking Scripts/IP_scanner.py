# Imports
import subprocess, re, sys
import ipaddress
from termcolor import colored
# import threading


# defining the scanner class
class Scanner():
    #initiating the class
    def __init__(self):
        pass
    
    # the Scan() function uses trial and error to scan all ports in a ip address
    def Scan(self, ip_address):
        
        # Converts the ip which is an integer into an ip (mainly because arethmetic is easier)
        # if the 24 value is increased then the ip's dislpayed will be halve, 
        # if the 24 value is decreased then the ip's displayed will increase
        # 25 is the perfect number as it will show all ip's without overlapping any
        address = ipaddress.ip_network((ip_address + '/24'), False)

        # for IP's in the router
        for ip in address.hosts():
            ping = subprocess.run(["ping", str(ip)], capture_output=True) # pings the ip
            result = re.findall( 'Reply', str(ping)) # finds a certain pattern in a string

            # This If - Else Statements checks if the ping was succesful
            if result != '[]':
                print(colored((f"[++] IP found: {result}"), 'green', attrs=['bold']))
            else:
                print(colored((f"[--] No IP Connected to Target With Address: {ip}"), 'red', attrs=['bold']))


    # Pings one ip address
    def ping(self, ip_address):
        
        # Try Execpt statement to avoid crashing the program
        try: 
            # try to ping 
            output = subprocess.run(['ping', ip_address], capture_output=True)
            result = re.findall(f"Destination host unreachable" ,str(output))

            # Checks if ping is sucsesslul
            if "Destination host unreachable" not in result:
                print(colored((f"[++] Connected IP Address: {ip_address}"), 'green', attrs=['bold']))

            else:
                print(colored((f"[--] No IP Connected To Router With Address of: {ip_address}"), 'red', attrs=['bold']))
        
        except Exception as e: print(colored((f"Error: {e}"),'red', attrs=['bold']))

    # pings all ip addresses in a range
    def pingRange(self, start_ip, end_ip):
        while start_ip != end_ip:
            # Calls pingFunction
            self.ping(start_ip)
            start_ip = (ipaddress.IPv4Address(start_ip)+1)
            start_ip = str(start_ip)

        

if '__main__' == __name__:

    bot = Scanner()
    bot.pingRange("192.168.1.95", "192.168.1.140")

# add = ipaddress.ip_network("192.168.1.1/24", strict=False)
# for ip in add.hosts():
#     print(ip)