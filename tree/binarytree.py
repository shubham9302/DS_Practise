from queue import Queue
import ctypes


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


class Tree:
    def __init__(self, root_node_val=None):
        self.root = None
        self.q = Queue(maxsize=0)
        self.root_node_val = root_node_val

    def createTree(self):
        if self.root is None:
            temp_node = Node(data=self.root_node_val)
            self.root = temp_node
            print("self.root", self.root.data)
            self.q.put(self.root)
            while not self.q.empty():
                temp_pointer = self.q.get()
                print("temp_pointer", temp_pointer.data)
                value = input("Enter the left child")

                if int(value) != -1:
                    new_node = Node(data=value)
                    temp_pointer.left = new_node
                    self.q.put(new_node)
                value = input("Enter the right child")
                if int(value) != -1:
                    new_node = Node(data=value)
                    temp_pointer.right = new_node
                    self.q.put(new_node)

    def preOrder(self, temp):
        # root -> left -> right
        # visit(node)->preorder(left)->preorder(right)
        if temp:
            print(temp.data)
            left_node = temp.left
            self.preOrder(left_node)
            right_node = temp.right
            self.preOrder(right_node)

    def inOrder(self, temp):
        # left -> root -> right
        # inorder(left) -> visit(node) -> inorder(right)
        if temp:
            self.inOrder(temp.left)
            print(temp.data)
            self.inOrder(temp.right)

    def postOrder(self, temp):
        # left -> right -> root
        # postOrder(left) -> postOrder(right) -> visit(node)
        if temp:
            self.postOrder(temp.left)
            self.postOrder(temp.right)
            print(temp.data)

    def preOrderIterative(self, root):
        dataset = list()
        temp = root
        print(temp.data)
        dataset.append(root)
        temp = temp.left
        while dataset or temp:
            if temp:
                print(temp.data)
                dataset.append(temp)
                temp = temp.left
            else:
                temp = dataset.pop()
                temp = temp.right

    def InOrderIterative(self, root):
        dataset = list()
        temp = root
        while dataset or temp:
            if temp:
                dataset.append(temp)
                temp = temp.left
            else:
                temp = dataset.pop()
                print(temp.data)
                temp = temp.right

    def postOrderIterative(self, root):
        rev = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    rev.append(node.data)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

    def levelOrderTraversal(self, root):
        dataset = Queue(maxsize=0)
        temp = root
        print(temp.data)
        dataset.put(temp)
        while not dataset.empty():
            p = dataset.get()
            left_child = p.left
            if left_child:
                print(left_child.data)
                dataset.put(left_child)
            right_child = p.right
            if right_child:
                print(right_child.data)
                dataset.put(right_child)


if __name__ == "__main__":
    t1 = Tree(root_node_val=10)
    t1.createTree()
    root = t1.root
    """
    sample input stream 
    self.root 8
    temp_pointer 8
    Enter the left child3
    Enter the right child9
    temp_pointer 3
    Enter the left child7
    Enter the right child-1
    temp_pointer 9
    Enter the left child6
    Enter the right child4
    temp_pointer 7
    Enter the left child5
    Enter the right child-1
    temp_pointer 6
    Enter the left child-1
    Enter the right child2
    temp_pointer 4
    Enter the left child-1
    Enter the right child-1
    temp_pointer 5
    Enter the left child-1
    Enter the right child-1
    temp_pointer 2
    Enter the left child-1
    Enter the right child-1
    """
    # t1.preOrder(root)
    # t1.preOrderIterative(root)
    # t1.InOrderIterative(root)
    # print("###")
    # t1.inOrder(root)
    # t1.postOrderIterative(root)
    t1.levelOrderTraversal(root)
