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
#INSERT NEWNODE AT BEGINING
new_node=node("G")
new_node.next=n1
n1=new_node

n1.print_list()

#INSERT AT END
new_node=node("C")
current=n1

while current.next is not None:
    current=current.next
        
current.next=new_node
        
n1.print_list()

#INSERT NEWNODE AT MIDDLE
current=n1
# while current is not None and current.name != givenvalue:
#     current=current.next
#   if current is None:
#       print("Above val not found")
#     new_node=node("L")
#     new_node.next=current.next 
#     current.next=ne_node
    



    


