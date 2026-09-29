#creation of a node
class node:
    def __init__(self,name):
        self.name=name
        self.next=None
        
    def print_list(self):
        current=self
        
        while current is not None:
            print(current.name)
            current=current.next
               
        
n1=node("A")
n2=node("B")
n3=node("C")

n1.next=n2
n2.next=n3

n1.print_list()


