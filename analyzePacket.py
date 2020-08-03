from scapy.all import *
import re

def analyzePacket(data, pairs_dict, write_lines, No):

    if(is_ipv4_icmp(data)):
        
        print(data.fields)
        print(getICMPPacket(data).fields)
        print(getICMPPayload(data))

        
        getICMPPair(data, pairs_dict, write_lines, No)

    #print(type(data.payload))  #==><class 'scapy.layers.inet.IP'>  可以使用 help(scapy.layers.inet.IP) 查看帮助文档

def is_ipv4_icmp(data):
    
    ip_packet = data.payload
    return data.fields['type'] == 2048 and ip_packet.fields['version'] == 4 and ip_packet.fields['proto'] == 1
    

def getIcmpLen(data):
    ip_packet = data.payload

    ip_header_len = ip_packet.fields['ihl'] * 4
    ip_len = ip_packet.fields['len']
    icmp_len = ip_len - ip_header_len
    return icmp_len

def getICMPPacket(data):
    ip_packet = data.payload
    icmp_packet = ip_packet.payload
    return icmp_packet

def getICMPPayload(data):
    ip_packet = data.payload
    icmp_packet = ip_packet.payload
    icmp_payload = icmp_packet.payload

    return str(icmp_payload.original)


def getICMPPair(data, pairs_dict, write_lines, No):
    ip_packet = data.payload
    icmp_packet = ip_packet.payload

    icmp_fileds = icmp_packet.fields
    ICMPLen = getIcmpLen(data)


    id = icmp_packet.fields['id']
    seq = icmp_packet.fields['seq']
    key = (id, seq)
    
    if key not in pairs_dict.keys():
        write_lines.append("\n")
        write_lines.append('key=' + str(key))
        pairs_dict[key] = []

    pairs_dict[key].append(icmp_packet)

    write_lines.append('No' + str(No) + ' ;ICMPLen=' + str(ICMPLen) + ' ;type=' + str(icmp_fileds['type']) + ' ;code=' + str(icmp_fileds['code']) + ' ;chksum=' + str(icmp_fileds['chksum']))
    write_lines.append(str(icmp_packet))

    





# analyzePcap('C:\\Users\\dong\\Desktop\\workAtHome\\vnc协议\\vnc_concise.pcap')
