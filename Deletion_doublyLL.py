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
            
    def delete_first(self):
        current=self
        
        current=current.next
        current.prev=None
        
        return current
     
    def delete_end(self):
        current=self
        
        while current.next is not None:
            current=current.next
            
        current=current.prev
        current.next=None
        return current
            
        
          
        
n1=node("A")
n2=node("B")
n3=node("C") 

n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2

n1.print_list()

n1=n1.delete_first()
print(n1)

n1=n1.dlete_end()
print(n1)
