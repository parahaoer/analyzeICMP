from scapy.all import *
import re
from LinkedHashMap import LinkedHashMap
from analyzePacket import analyzePacket



def analyzePcap(filepath):

    global linkedHashMap

    s1 = PcapReader(filepath)

    No = 1
    # try:
        # data 是以太网 数据包
    data = s1.read_packet()

    while data is not None:

        analyzePacket(data, linkedHashMap)
        data = s1.read_packet() 
        No += 1

    s1.close()
    # except Exception as ex:
    #     print(ex)

    #print(type(data.payload))  #==><class 'scapy.layers.inet.IP'>  可以使用 help(scapy.layers.inet.IP) 查看帮助文档

def get_filelist(dir):

    if os.path.isfile(dir):
        try:
            analyzePcap(dir)        
        except Scapy_Exception as e:
            pass

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir)

linkedHashMap  = LinkedHashMap()
get_filelist('PingTunnel')



