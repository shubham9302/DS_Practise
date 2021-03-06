from array import array


class Node:
    def __init__(self, value=None, next=None):
        self.data = value
        self.next = next


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

    def getLength(self):
        counter = 0
        temp = self.head
        while temp:
            temp = temp.next
            counter += 1
        return counter

    def printList(self):
        counter = 0
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            counter += 1
        return counter

    def printListWithRecursion(self, head):
        if head is not None:
            print(head.data)
            temp = head.next
            self.printListWithRecursion(temp)

    def printReverseList(self, head):
        if head is not None:
            temp = head.next
            self.printReverseList(temp)
            print(head.data)

    def sumOfAllElements(self):
        sumdata = 0
        temp = self.head
        while temp:
            value = temp.data
            temp = temp.next
            sumdata += value
        return sumdata

    def maxElement(self):
        maxval = float('-inf')
        temp = self.head
        while temp:
            value = temp.data
            temp = temp.next
            if value > maxval:
                maxval = value
        return maxval

    def searchElement(self, data):
        temp = self.head
        while temp:
            value = temp.data
            if value == data:
                return temp
            temp = temp.next
        return temp

    def InsertAtPosition(self, position_element, value):
        temp = self.head
        if position_element == 0:
            return self.insertElementatHead(value)
        if position_element >= self.getLength():
            raise IndexError
        counter = -1
        while temp:
            counter += 1
            if counter == position_element:
                next_node_adress = temp.next
                temp.next = Node(value)
                temp.next.next = next_node_adress
                return temp
            temp = temp.next
        return temp

    def insertElement(self, position=None, value=None):

        temp = self.head
        counter = 1
        while temp:
            # counter += 1
            if position == 0:
                self.insertElementatHead(value)
                break
            elif counter == position and position < self.getLength():
                next_node_adress = temp.next
                temp.next = Node(value, next_node_adress)
                break
            counter += 1
            temp = temp.next

    def insertElementatHead(self, value):
        val = Node(value)
        val.next = self.head
        self.head = val

    def printLinkedListRecursive(self, l1):
        temp = l1.head
        if temp is not None:
            l1.head = temp.next
            print(temp.data)
            self.printLinkedListRecursive(l1)

    def insertInSortedList(self, value=None):
        tail_pointer = None
        head_pointer = self.head
        counter = 0
        while head_pointer:
            data = head_pointer.data
            if value > data:
                tail_pointer = head_pointer
                head_pointer = head_pointer.next
                counter += 1
            elif counter == 0:
                self.insertElementatHead(value)
                break

            else:
                temp = Node(value, head_pointer)
                # temp.next = head_pointer
                tail_pointer.next = temp
                counter += 1
                break
        if counter == self.getLength():
            temp = Node(value, None)
            tail_pointer.next = temp

    def deleteHeadNode(self):

        temp = self.head.next
        self.head.next = None
        self.head = temp

    def deleteNodeAtPosition(self, position=None):
        temp = self.head
        tail_counter = None
        counter = 0
        original_length = self.getLength()
        while temp:
            if position == 0:
                self.deleteHeadNode()
                break
            elif counter == position and counter < self.getLength():
                tail_counter.next = temp.next
                break
            else:
                tail_counter = temp
                temp = temp.next
                counter += 1
        if counter >= original_length:
            raise Exception

    def isSorted(self):
        temp = self.head
        min_val = float('-inf')
        val = True
        while temp:
            data = temp.data
            if data > min_val:
                temp = temp.next
                min_val = data

            else:
                val = False
                break
        return val

    def reverseLinkListWithReverseNumbers(self):
        linked_list_size = self.getLength()
        additional_arr = array("i", [0] * linked_list_size)
        counter = 0
        temp = self.head
        while temp and counter < linked_list_size:
            additional_arr[counter] = temp.data
            temp = temp.next
            counter += 1
        temp = self.head
        counter -= 1
        while temp and counter >= 0:
            temp.data = additional_arr[counter]
            temp = temp.next
            counter -= 1

    def reverseLinkListWithReverseLinks(self):
        r = None
        q = None
        p = self.head
        while p is not None:
            r = q
            q = p
            p = p.next
            q.next = r
        self.head = q

    def concateLinkedList(self, ldata=None):

        self.tail.next = ldata.head

    def merge2sortedLinkedList(self, ldata1=None, ldata2=None):
        first = ldata1.head
        second = ldata2.head
        third = None
        last = None

        if first.data < second.data:
            third = first
            last = first

            first = first.next
            last.next = None
        else:
            third = second
            last = second

            second = second.next
            last.next = None
        while first is not None and second is not None:
            if first.data < second.data:
                last.next = first
                last = first
                first = first.next
                last.next = None
            else:
                last.next = second
                last = second
                second = second.next
                last.next = None
        if first is not None:
            last.next = first
        else:
            last.next = second
        self.head = third


if __name__ == "__main__":
    t1 = LinkedListImp()
    t1.addElement(2)
    t1.addElement(14)
    t1.addElement(16)
    t1.addElement(18)
    val = t1.head

    t2 = LinkedListImp()
    t2.addElement(1)
    t2.addElement(15)
    t2.addElement(47)
    t2.addElement(17)
    # t1.printLinkedListRecursive(t1)
    # print(t1.printListWithLength())
    # print(t1.sumOfAllElements())
    # print(t1.maxElement())
    # print(t1.searchElement(32768))
    # print(t1.insertElement(1, 61))
    # print(t1.printList())
    # print(t1.insertElementatHead(8))
    # print(t1.printList())
    # print(t1.insertElementatHead(101))
    # print(t1.printListWithLength())
    # t1.insertInSortedList(15)
    # t1.insertInSortedList(10)
    # t1.insertInSortedList(1)
    # print(t1.printList())
    # print("#####")
    # t1.deleteHeadNode()
    # print(t1.printList())
    # print("####")
    # t1.deleteNodeAtPosition(2)
    # print("$$$$$")
    # print(t1.printList())
    # print(t1.isSorted())
    # print(t1.reverseLinkListWithReverseNumbers())
    print(t1.reverseLinkListWithReverseLinks())
    # print(t1.concateLinkedList(ldata=t2))
    #t3 = LinkedListImp()
    #t3.merge2sortedLinkedList(t1, t2)

    print(t1.printList())
