from array import array


class Node:
    def __init__(self, value=None, next=None):
        self.data = value
        self.next = next


class CircularLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insertElement(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
            self.tail.next = self.head
        else:
            temp = Node(value)
            self.tail.next = temp
            self.tail = self.tail.next
            self.tail.next = self.head

    def getLength(self):
        counter = 1
        initial = self.head
        temp = initial.next
        while temp != initial:
            value = temp.data
            temp = temp.next
            counter += 1
        return counter

    def printList(self):
        initial = self.head
        temp = initial.next
        print(initial.data)
        while temp != initial:
            value = temp.data
            print(value)
            temp = temp.next

    def insertElementAtPosition(self, value=None, position=None):
        initial = self.head
        tail_counter = initial
        temp = initial.next
        counter = 1
        initial_length = self.getLength()
        if position == 0:
            next_node_adress = self.head
            self.head = Node(value, next_node_adress)
            self.tail.next = self.head
        elif position >= initial_length:
            raise IndexError
        else:
            while temp != initial:
                if counter == position:
                    next_node_adress = temp
                    tail_counter.next = Node(value, next_node_adress)
                    break
                elif counter < initial_length:
                    counter += 1
                    tail_counter = temp
                    temp = temp.next

    def deletenodeatposition(self, position=None):
        tail_pointer = None
        temp = self.head
        listLength = self.getLength()
        counter = 0
        while temp:
            if position == 0:
                next_node = temp.next
                self.tail.next = next_node
                self.head = next_node
                break
            elif position == listLength - 1 and position == counter:
                self.tail = tail_pointer
                self.tail.next = self.head
                break
            elif position == counter:
                next_node = temp.next
                tail_pointer.next = next_node
                break
            else:
                tail_pointer = temp
                temp = temp.next
                counter += 1


if __name__ == "__main__":
    t1 = CircularLinkedList()
    t1.insertElement(2)
    t1.insertElement(3)
    t1.insertElement(7)
    t1.insertElement(9)
    t1.printList()
    print("$$$$$$$$")
    t1.insertElementAtPosition(5, 0)
    t1.printList()
    t1.deletenodeatposition(1)
    print("$$$$$$")
    t1.printList()
