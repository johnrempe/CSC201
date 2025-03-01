# LinkedList class
# I have given you the basic structure of the class.
# TO DO: Complete the methods that have "pass" in their places
# and add comments for each method - 1 or 2 lines saying what it does
# Then test it using the LL_Tester file before doing the assignment
# YOUR NAME: John Rempe

from Node import Node

class LinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._curr = Node()
    
    #changes or returns where the pointers are pointing
    #we use these instead of normal getters/setters so folks don't mess with our pointers
    # here = a Node object
    def setHead(self, here):
        self._head.link = here
    def getHead(self):
        return self._head.link
    def setTail(self, here):
        self._tail.link = here
    def getTail(self):
        return self._tail.link
    def setCurr(self, here):
        self._curr.link = here
    def getCurr(self):
        return self._curr.link
    
    def isEmpty(self):
        if self.getHead() == None:
            return True
        return False
    
    def isBeginning(self):
        if self.getCurr() == self.getHead():
            return True
        return False
    
    def isEnd(self):
        if self.getCurr() == self.getTail():
            return True
        return False
    
    def goBeginning(self):
        self.setCurr(self._head.link)
    
    def goEnd(self):
        self.setCurr(self._tail.link)
        
    def getSize(self):
        current = self.setCurr(self._head.link)
        count = 0
        while current != None:
            count += 1
            current.goNext()
        return count
    
    def getPos(self):
        #returns the current position as a number
        if self.isEmpty():
            return -1
        elif self.getHead() == self.getCurr():
            return 0
        temp = self.getHead()
        pos = 0
        while temp != self.getCurr():
            pos += 1
            temp = temp.link
        return pos
    
    def setPos(self, pos):
        self.setCurr(self.getHead())
        for i in range(pos):
            self.setCurr(self.goNext())
                
    def goNext(self):
        if self.getCurr().link != None:
            return self.setCurr(self.getCurr().link)
    
    def goPrev(self):
        if self.getCurr() == self.getHead():
            return
        prev = self.getHead()
        while prev.link != self.getCurr():
            prev = prev.link
        self.setCurr(prev)
        
    def getData(self):
        return self.getCurr().data
    
    def setData(self, d):
        self.getCurr().data = d
    
    def insert(self, n):
        #inserts a new node, n, after the curr.link node
        n.link = self.getCurr().link
        self.getCurr().link = n
        if n.link == None:
            self.setTail(n)
            
    def append(self, n):
        #inserts at the end of the list
        if self.isEmpty():
            self.setHead(n)
            self.setTail(n)
        else:
            self.getTail().link = n
            self.setTail(n)
            
            
    def insertBefore(self, n):
        # inserts before curr
        if self.getCurr() == self.getHead():
            n.link = self.getCurr()
            self.setHead(n)
            self.setTail(self.getCurr())
        else:
            prev = self.getHead()
            while prev.link != self.getCurr():
                prev = prev.link
            n.link = self.getCurr()
            prev.link = n
            
    
    def remove(self, item):
        #removes the node at curr
        current = self.setCurr(self._head.link)
        prev = None
        found = False
        while found != True:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.goNext()
        prev.link = current.link
        current.setData(None)
        self.setCurr(prev)
    
    def copy(self):
        #copies the list and returns a new list
        self.setCurr(self._head.link)
        temp = LinkedList()
        while self._curr.link != None:
            n = Node(self._curr.link.data)
            temp.append(n)
            self.setCurr(self._curr.link.link)
        return temp
    
    def __str__(self):
        self.setCurr(self._head.link)
        s = ""
        while self._curr.link != None:
            s += str(self._curr.link.data)
            s += "  "
            self.setCurr(self._curr.link.link)
        return s
