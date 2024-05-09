import random
import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def minValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.minValueNode(node.left)

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        # Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        # Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


# Usage

random.seed(1)
data = list(range(0, 100_000_000))
random.shuffle(data)

sizes = [500_000,1_000_000,5_000_000,10_000_000]
samp_num = 500_000
#sampler = random.sample(data,samp_num)

for i in sizes:
    sampler = random.sample(data[0:i],samp_num)
    avl = AVLTree()
    root = None

    # Insert elements
    time_start_insert = time.time()
    for key in data[0:i]:
        root = avl.insert(root, key)
    time_end_insert = time.time()
    print(f"Time to insert {i} = {time_end_insert - time_start_insert} seconds")

    # Search for random elements
    #elements_to_search = random.sample(data, samp_num)
    time_start_search = time.time()
    for key in sampler:
        avl.search(root, key)
    time_end_search = time.time()
    print(f"Time to search {samp_num} random elements = {time_end_search - time_start_search} seconds")

    # Delete random elements
    #elements_to_delete = random.sample(data, samp_num)
    time_start_delete = time.time()
    for key in sampler:
        root = avl.delete(root, key)
    time_end_delete = time.time()
    print(f"Time to delete {samp_num} random elements = {time_end_delete - time_start_delete} seconds")
    del avl
    print("------------------------------------------------------------")
