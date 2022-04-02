class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, value=None):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:

            temp = Node(value)
            self.tail.next = temp
            self.tail = temp

    def getLength(self):
        counter = 0
        temp = self.head
        while temp:
            temp = temp.next
            counter += 1
        return counter

    def printList(self):
        temp = self.head
        while temp:
            value = temp.data
            print(value)
            temp = temp.next

    def deleteNNodesAfterMNodes(self, m=None, n=None):
        base_counter = 0
        delete_counter = 0
        temp = self.head
        while temp:
            if base_counter < m - 1:
                base_counter += 1
                print("base_counter", base_counter)
            elif base_counter == m - 1:
                temp_node = temp
                print("temp_node", temp_node.data)
                while delete_counter < n and temp_node.next:
                    temp_node = temp_node.next
                    delete_counter += 1
                    print("temp_node_delete", temp_node.data)
                temp.next = temp_node.next
                base_counter = 0
                delete_counter = 0
            temp = temp.next

    def deleteNodeWithVal(self, value=None):
        temp = self.head
        tail_pointer = None
        position = 0
        while temp:
            if position == 0 and temp.data == value:
                additional = self.head.next
                self.head.next = None
                self.head = additional
                position += 1

            elif temp.data == value:
                next_node = temp.next
                tail_pointer.next = next_node
                temp = tail_pointer.next
            else:

                tail_pointer = temp
                temp = temp.next
                position += 1

    def middleOfLinkedList(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        print("middle", slow_pointer.data)

    def intersectionbetween2list(self, t1, t2):
        temp = t1.head
        while temp:
            temp_t2 = t2.head
            while temp_t2:
                if temp_t2 == temp:
                    return temp.data
                else:
                    temp_t2 = temp_t2.next
            temp = temp.next

    def intersectionopt(self, t1, t2):
        temp = t1.head
        temp_2 = t2.head
        temp_adress = list()
        temp_2_adress = list()
        while temp:
            temp_adress.append(temp_2)
            temp = temp.next
        while temp_2:
            temp_2_adress.append(temp_2)
            temp_2 = temp_2.next

        while len(temp_2_adress) > 0 or len(temp_adress):
            temp_val = temp_adress.pop()
            tem2_val = temp_2_adress.pop()
            if temp_val == tem2_val:
                return True


if __name__ == "__main__":
    t1 = LinkedList()
    t1.append(1)
    t1.append(2)
    t1.append(3)
    t1.append(4)
    t1.append(5)
    t1.append(6)

    t2 = LinkedList()
    t1.append(11)
    t1.append(21)
    t1.append(31)
    t1.append(4)
    t1.append(55)
    t1.append(66)

    # t1.printList()
    # t1.deleteNNodesAfterMNodes(2, 2)
    # t1.printList()
    t1.middleOfLinkedList()
    # t1.solution2(2, 2)
    # print("$$$$")
    # t1.printList()
    # print("####")
    # t1.deleteNodeWithVal(3)
    # print("####")
    # t1.printList()
