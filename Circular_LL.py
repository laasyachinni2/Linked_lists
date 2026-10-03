 #creation of a node
class node:
    def __init__(self,name):
        self.name=name
        self.next=None
        
    def print_list(self):
        current=self
        
        while current.next != self:                         
            print(current.name)
            current=current.next   
            
        print(current.name)  
        
        #ALternative printing
        # while True:
        #     print(current.data) 
        #     current=current.next
            
        #     if current==self:
        #         break 
               
        
n1=node("A")
n2=node("B")
n3=node("C")

n1.next=n2
n2.next=n3
n3.next=n1
 
n1.print_list()


