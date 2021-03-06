import copy
import sys


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

    def printList(self, head):
        temp = head
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

    def delete(self, value=None):
        temp = self.head
        tail_pointer = None
        pos = 0
        while temp:
            data = temp.data
            if pos == 0 and value == self.head.data:
                self.head = None
                self.head = temp.next
                temp = self.head

            elif data == value:
                tail_pointer.next = temp.next
                temp = tail_pointer.next
                pos += 1
            else:
                tail_pointer = temp
                temp = temp.next
                pos += 1

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

    def reverseLinkedList(self, head):
        r = None
        q = None
        p = head
        while p is not None:
            r = q
            q = p
            p = p.next
            q.next = r
        head = q
        return head

    def isPalindrome(self, head):
        original = copy.deepcopy(head)
        reversedList = self.reverseLinkedList(head)
        temp_2 = reversedList
        self.printList(temp_2)
        print("####")
        self.printList(original)
        temp = original
        while temp:
            print("temp_2.data", temp_2.data)
            print("temp.data", temp.data)
            if temp_2.data != temp.data:
                print("inside if")
                print("temp_2.data", temp_2.data)
                print("temp.data", temp.data)
                return False
            temp_2 = temp_2.next
            temp = temp.next
        return True

    def ispalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = slow
        slow = slow.next
        prev.next = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        fast = head
        slow = prev
        while slow:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

    def getIntersectionNode(self, headA, headB):
        temp = headA
        temp_2 = headB
        while temp and temp_2:
            if temp == temp_2:
                return temp.data
            temp = temp.next
            temp_2 = temp_2.next
        return None

    def deleteDuplicates(self):
        temp = self.head
        tail_pointer = None
        data = list()
        while temp:
            if temp.data in data:
                tail_pointer.next = temp.next
                temp = temp.next
            else:
                data.append(temp.data)
                tail_pointer = temp
                temp = temp.next

    def oddList(self, head):
        # [1,2,3,4,5,6,7]
        odd_pointer = head
        while odd_pointer and odd_pointer.next:
            next_next_node = odd_pointer.next.next
            odd_pointer.next = next_next_node
            odd_pointer = next_next_node
        return head

    def evenList(self, head):
        head = head.next
        even_pointer = head
        while even_pointer and even_pointer.next:
            next_next_node = even_pointer.next.next
            even_pointer.next = next_next_node
            even_pointer = next_next_node
        return head

    def oddEvenList(self, head):
        odd_pointer = head
        temp_odd_head = odd_pointer.next

        # print("temp_odd_head.next.data",temp_odd_head.next.data)
        tail_odd_pointer = None

        while odd_pointer and odd_pointer.next:
            next_next_node = odd_pointer.next.next
            odd_pointer.next = next_next_node
            tail_odd_pointer = odd_pointer
            odd_pointer = next_next_node

        even_pointer = temp_odd_head
        # print(even_pointer.data)
        temp_head = even_pointer
        while even_pointer and even_pointer.next:
            next_next_node = even_pointer.next.next
            even_pointer.next = next_next_node
            even_pointer = next_next_node

        # self.printList(temp_head)
        # tail_odd_pointer.next = temp_odd_head
        return temp_head

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False


if __name__ == "__main__":
    t1 = LinkedList()
    t1.append(1)
    t1.append(2)
    t1.append(3)
    t1.append(4)
    t1.append(5)
    t1.append(6)
    t2 = LinkedList()
    t2.append(1)
    t2.append(1)
    t2.append(2)
    t2.append(1)

    # t1.printList()
    # t1.deleteNNodesAfterMNodes(2, 2)
    # t1.printList()
    # t1.middleOfLinkedList()
    # t1.solution2(2, 2)
    # print("$$$$")
    # t1.printList()
    # print("####")
    # t1.delete(3)
    # print("####")
    # t1.printList()
    common = Node(15)

    # Defining first LinkedList

    head1 = Node(3)
    head1.next = Node(6)
    head1.next.next = Node(9)
    head1.next.next.next = common
    head1.next.next.next.next = Node(30)
    reversedListA = t1.reverseLinkedList(head1)

    # Defining second LinkedList

    head2 = Node(10)
    head2.next = common
    head2.next.next = Node(30)
    reversedListB = t1.reverseLinkedList(head2)
    # print(t1.getIntersectionNode(reversedListA, reversedListB))
    # t1.delete(3)
    # t1.printList(t1.head)
    val = t1.oddEvenList(t1.head)
    t1.printList(val)
