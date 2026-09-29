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
            
     #Delete node at first       
    def delete_first(self):
        current=self
        if current is None:
            return None
        
        current=current.next 
        return current
    
    def delete_last(self):
        current=self
        if current is None:
            return None
        
        if current.next is None:
            return None
        
        while current.next.next is not None:
            current=current.next
            
        current.next=None
        return current
    
    # def delete_given(self):
    #     current=self
    #     if current is None:
    #         return None
        
    #     while current.next.name != given and current.next is not None:
    #         current=current.next
            
    #         current.next=current.next.next 
    #         return current
            
                     
        
n1=node("A")
n2=node("B")
n3=node("C")

n1.next=n2
n2.next=n3
n1.print_list()

n1=n1.delete_first()
n1.print_list()

n1=n1.delete_last()
n1.print_list()

n1=n1.delete_given()
n1.print_list()




