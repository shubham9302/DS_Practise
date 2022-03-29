class Node:
    def __init__(self, value=None, next=None, previous=None):
        self.data = value
        self.next = next
        self.previous = previous


class DoublyLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, value=None):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            previous_node_adress = self.tail
            self.tail = Node(value=value, previous=previous_node_adress)
            previous_node_adress.next = self.tail

    def printList(self):
        temp = self.head
        while temp:
            value = temp.data
            print(value)
            temp = temp.next

    def insertElement(self, value=None, position=None):
        tail_pointer = None
        temp = self.head
        counter = 0
        length = self.getLength()
        while temp:
            if position == 0:
                self.head = Node(value, next=temp)
                break
            elif position == counter and position == length - 1:
                self.append(value=value)
                break

            elif position == counter:
                node_val = Node(value=value, next=temp, previous=tail_pointer)
                tail_pointer.next = node_val
                break
            else:
                tail_pointer = temp
                temp = temp.next
                counter += 1

    def getLength(self):
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            temp = temp.next
        return counter

    def deleteNodeAtPosition(self, position=None):
        tail_pointer = None
        temp = self.head
        counter = 0
        length = self.getLength()
        while temp:
            if position == 0:
                next_node = temp.next
                self.head = next_node
                self.head.previous = None
                break

            elif position == counter and position == length - 1:
                self.tail = tail_pointer
                self.tail.next = None
                break
            elif position == counter:
                temp.next.previous = tail_pointer
                tail_pointer.next = temp.next
                break
            else:
                tail_pointer = temp
                temp = temp.next
                counter += 1


if __name__ == "__main__":
    t1 = DoublyLinkedList()
    t1.append(2)
    t1.append(3)
    t1.append(4)
    t1.append(5)
    t1.insertElement(1, 2)
    t1.printList()
    print("$$$$$$$")
    t1.deleteNodeAtPosition(3)
    print("%%%%%%")
    t1.printList()
