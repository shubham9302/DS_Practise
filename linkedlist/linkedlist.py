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

    def printListWithLength(self):
        counter = 0
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            counter += 1
        return counter

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
        while temp:
            data = temp.data
            if data == position_element:
                next_node_adress = temp.next
                temp.next = Node(value)
                temp.next.next = next_node_adress
                return temp
            temp = temp.next
        return temp

    def insertElementatHead(self,value):
        val = Node(value)
        val.next = self.head
        self.head = val




if __name__ == "__main__":
    t1 = LinkedListImp()
    t1.addElement(2)
    t1.addElement(-4)
    t1.addElement(32768)
    #print(t1.printListWithLength())
    # print(t1.sumOfAllElements())
    # print(t1.maxElement())
    #print(t1.searchElement(32768))
    #print(t1.InsertAtPosition(-4, 6))
    #print(t1.printListWithLength())
    print(t1.insertElementatHead(8))
    print(t1.printListWithLength())
    print(t1.insertElementatHead(101))
    print(t1.printListWithLength())
