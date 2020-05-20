#A single node that holds Data and Point to the next node
class node:
    #Constructor
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        
#Creating a single node
first=node(3)
#Creating A linkedList with a single head node
class LinkedList:
    def __init__(self):
        self.head=None
##linkedList with a single head node
#LL=LinkedList()
#LL.head=node(3)
#print(LL.head.data)
        
#insertion methods
    def insert(self,data):
        newNode=node(data)
        if(self.head):
            current=self.head
            while(current.next):
                current=current.next
            current.next=newNode
        else:
            self.head=newNode

#print method
    def print(self):
        current=self.head
        while(current):
            print(current.data)
            current=current.next
LL=LinkedList()
LL.insert(3)
LL.insert(5)
LL.insert(6)
LL.insert(9)
LL.print()


            

