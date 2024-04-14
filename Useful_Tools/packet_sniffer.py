import scapy.all as scapy
from scapy.all import sniff



def sniff(interface):
    scapy.sniff(iface=interface,prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    packet.show()
sniff("eth0")
