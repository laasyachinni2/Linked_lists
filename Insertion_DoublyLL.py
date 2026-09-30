                                                                                 #creation of a node
class node:
    def __init__(self,name):
        self.name=name
        self.prev=None
        self.next=None
        
    def print_list(self):
        current=self
        
        while current is not None:
            print(current.name)
            current=current.next
            
    def insert_first(self,new_node):
        current=self
        
        new_node.next=current
        current.prev=new_node
        return new_node
    
    def insert_end(self,new_node):
        current=self
        
        while current.next is not None:
            current=current.next
            
        current.next=new_node
        new_node.prev=current
        return new_node
        
        
n1=node("A")
n2=node("B")
n3=node("C") 

n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2

n1.print_list()

new_node=node("D")
n1=n1.insert_first(new_node)
n1.print_list()

new_node=node("E")
n1=n1.insert_end(new_node)
n1.print_list()
