from DoubleList import DoubleList
from Node import Node
class LinkedHashMap():
    
    def __init__(self):
        self.dict = {}
        self.doublelist = DoubleList()

    def add(self, id, seq, value):
        
        x = Node(id, seq)
        key = (id, seq)
        if(key not in self.dict):
            self.doublelist.addLast(x)
        else:

        #别忘了在 map 中添加 key 的映射
        self.dict[key].append(value)
    
    def deleteKey(self, key):

        x = self.dict[key]
        self.doublelist.remove(x)
        #从 map 中删除
        del self.dict[key]