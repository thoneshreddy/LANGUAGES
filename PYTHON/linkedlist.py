class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=node(data)
        if(not self.head):
            self.head=new_node
        else:
            current=self.head
            while(current.next):
                current=current.next
            current.next=new_node
    def display(self):
        current=self.head
        l=[]
        while(current):
            print(current.data,end="--->")
            current=current.next
        print("None")
        
            
llist=linkedlist()
llist.insert(10)
llist.insert(10)
llist.insert(30)
llist.insert(40)
llist.display()