from scapy.all import *
import re
from analyzePacket import analyzePacket



def analyzePcap(filepath):

    global pairs_dict
    global write_lines


    s1 = PcapReader(filepath)

    No = 1
    write_lines.append('filepath=' + filepath)


    try:
        # data 是以太网 数据包
        data = s1.read_packet()
    
        while data is not None:


            analyzePacket(data, pairs_dict, write_lines, No)
            data = s1.read_packet() 

            No += 1

        s1.close()
    except Exception as ex:
        print(filepath)
        print(No)
        print(ex)

    #print(type(data.payload))  #==><class 'scapy.layers.inet.IP'>  可以使用 help(scapy.layers.inet.IP) 查看帮助文档

def get_filelist(dir):

    if os.path.isfile(dir):
        try:
            analyzePcap(dir)        
        except Scapy_Exception as e:
            print(e)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir)

pairs_dict = {}
write_lines = []
get_filelist('PingTunnel')

ftxt = open("output.txt", 'a', encoding="utf-8")

for line in write_lines:
    ftxt.write(line + '\n')
ftxt.close



