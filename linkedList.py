
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class linkedList:
    def __init__(self):
        self.head=None

    def insertbeginning(self,data):
        node=Node(data,self.head)
        self.head=node
        return

    def inserAfter(self,data,afterdata):
        temp=self.head
        while temp.data!=afterdata:
            temp=temp.next
        node=Node(data,temp.next)
        temp.next=node
    
    def insertEnd(self,data):
        if self.head is None:
            self.insertbeginning(data)
            return

        temp=self.head
        
        while temp.next is not None:
            temp=temp.next
        
        node=Node(data,temp.next)
        temp.next=node
    
    def traverse(self):
        if self.head is None:
            print("Linked list empty")
            return

        temp=self.head
        
        while temp is not None:
            print(temp.data,end="-->")
            temp=temp.next
        print('END')

    def length(self):
        count=0
        temp=self.head
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    
    def remove(self,data):
        temp=self.head
        #Remove first Node
        if temp.data==data:
            if self.head.next is not None:
                self.head=self.head.next
                return
            elif self.head.next is None:
                self.head=None
                return

        #Removing others
        while temp!=None and temp.next.data!=data :
            temp=temp.next

        #if element not found in list
        if temp is None:
            return -1
        else:
            prev=temp
            nextNode=temp.next.next
            prev.next=nextNode
        
    def search(self,target):
        temp=self.head
        while (temp is not None) and (temp.data!=target)  :
            temp=temp.next
        if temp is None:
            return False
        else:
            return True
            



ll=linkedList()
ll.insertbeginning(1)
ll.insertbeginning(2)
ll.insertbeginning(3)
ll.inserAfter(4,1)
ll.insertEnd(10)
ll.insertEnd(5)
ll.traverse()



