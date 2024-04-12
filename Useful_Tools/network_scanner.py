import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("--target","--t", dest = "target",help = "Type your target IP Range!")
    (options,arguments)=parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target range ,write --help for more info")
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    
    answered_list = scapy.srp(arp_request_broadcast, timeout = 3)[0]
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip":element[1].psrc ,"mac":element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list
def print_result(results_list):
    print("-----------------------------------------\nIP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"]+"\t\t"+client["mac"])
        print("*****************************************")

    #print(arp_request_broadcast.summary())
    #arp_request_broadcast.show()
    #scapy.ls(scapy.ARP())
option = get_arguments()
if option != None:
    
   scan_result = scan(option.target)
   print_result(scan_result)
else:
    print("[-] Please write --help for more info ")
