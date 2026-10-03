 #creation of a node
class node:
    def __init__(self,name):
        self.name=name
        self.next=None
        
    def print_list(self):
        current=self
        
        while True:
            print(current.name) 
            current=current.next
            
            if current==self:
                break 
    
    def insert_last(self,new_node):
        current=self
        
        while current.next != self:
            current=current.next
            
        new_node.next=current.next
        current.next=new_node
        
    def insert_first(self,new_node):
        current=self
           
        while current.next != self:
               current=current.next
               
        new_node.next=self
        current.next=new_node
        
        return new_node
        
               
        
n1=node("A")
n2=node("B")
n3=node("C")

n1.next=n2
n2.next=n3
n3.next=n1
 
n1.print_list()

new_node=node("D")
n1.insert_last(new_node)

n1.print_list()

new_node=node("E")
n1=n1.insert_first(new_node)
n1.print_list()



