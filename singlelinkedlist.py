class node(object):
    def __init__(self,data=None,next=None) -> None:
        self.data  = data
        self.next = next

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self,new_next):
        self.next = new_next

class linkedlist(object):
    def __init__(self,head=None) -> None:
        self.head = head

    def insert(self,data):
        new_node = node(data)
        new_node.set_next(self.head)
        self.head = new_node
        print("Node with data " + str(data) + " is created succesfully")

    def size(self):
        count = 0
        while self.head:
            count+=1
            self.head = self.head.get_next()
        print("Size of link list is " + str(count))

    def searching(self,data):
        while self.head:
            if data == self.head.data:
                print("Node with data " + str(data) + " is found")
                break
            elif self.head == None:
                print("Node with data " + str(data) + " is not present")
                break
            else:
                self.head = self.head.get_next()

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            print("Node with data " + str(data) + " is not in list")
        elif previous is None:
            self.head = current.get_next()
            print("Node with data " + str(data) + " is deleted successfully")
        else:
            previous.set_next(current.get_next())
            print("Node with data " + str(data) + " is deleted successfully")


if __name__ == "__main__":
    obj = linkedlist()
    obj.insert(10)
    obj.insert(20)
    obj.insert(30)
    obj.insert(40)
    obj.insert(50)
    obj.insert(60)
    obj.searching(50)
    obj.size()
    


