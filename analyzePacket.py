from scapy.all import *
import re
from Node import Node

def analyzePacket(data, linkedHashMap):

    if(is_ipv4_icmp(data)):
        print(data.payload.payload.fields)
        print(getICMPPacket(data))
        print(getICMPPayload(data))
        print('ICMPIcmpLen =' + str(getIcmpLen(data)) + "\n")
        getICMPPair(data, linkedHashMap)

    #print(type(data.payload))  #==><class 'scapy.layers.inet.IP'>  可以使用 help(scapy.layers.inet.IP) 查看帮助文档

def is_ipv4_icmp(data):
    
    ip_packet = data.payload
    return ip_packet.fields['version'] == 4 and ip_packet.fields['proto'] == 1
    

def getIcmpLen(data):
    ip_packet = data.payload
    tcp_packet = ip_packet.payload

    ip_header_len = ip_packet.fields['ihl'] * 4
    ip_len = ip_packet.fields['len']
    icmp_len = ip_len - ip_header_len
    return icmp_len

def getICMPPacket(data):
    ip_packet = data.payload
    icmp_packet = ip_packet.payload
    return icmp_packet.original

def getICMPPayload(data):
    ip_packet = data.payload
    icmp_packet = ip_packet.payload
    icmp_payload = icmp_packet.payload

    return str(icmp_payload.original)


def getICMPPair(data, linkedHashMap):
    ip_packet = data.payload
    icmp_packet = ip_packet.payload
    id = icmp_packet.fields['id']
    seq = icmp_packet.fields['seq']
    linkedHashMap.add(id, seq, icmp_packet)
    





# analyzePcap('C:\\Users\\dong\\Desktop\\workAtHome\\vnc协议\\vnc_concise.pcap')
