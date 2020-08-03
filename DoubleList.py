from Node import Node
class DoubleList():
    
    def __init__(self):
        self.head = Node(0, 0, 0)
        self.tail = Node(0, 0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    #在链表尾部添加节点 x，时间 O(1)
    def addLast(self, x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size = self.size + 1    
    

    #删除链表中的 x 节点（x 一定存在）
    #由于是双链表且给的是目标 Node 节点，时间 O(1)
    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size = self.size - 1
    

    #删除链表中第一个节点，并返回该节点，时间 O(1)
    def removeFirst(self):
        if (self.head.next == self.tail):
            return null
        first = self.head.next
        self.remove(first)
        return first
    

    #返回链表长度，时间 O(1)
    def size(self):
        return self.size
    

    

