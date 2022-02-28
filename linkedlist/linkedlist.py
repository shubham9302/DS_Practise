class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None


class LinkedListImp:

    def __init__(self):
        self.head = None
        self.tail = None

    def addElement(self, value=''):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    t1 = LinkedListImp()
    t1.addElement(23)
    t1.addElement(78)
    t1.addElement(68)
    t1.printList()
