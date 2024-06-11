class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None


    def insert(root, key):
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = Node.insert(root.left, key)
        else:
            root.right = Node.insert(root.right, key)
        return root


    def search(root, key):
        if root is None:
            return False
        elif key < root.key:
            return Node.search(root.left, key)
        elif key > root.key:
            return Node.search(root.right, key)
        else:
            return True


    def preorder_traversal(root):
        if root is not None:
            print(root.key)
            Node.preorder_traversal(root.left)
            Node.preorder_traversal(root.right)


    def inorder_traversal(root):
        if root is not None:
            Node.inorder_traversal(root.left)
            print(root.key)
            Node.inorder_traversal(root.right)

  
    def postorder_traversal(root):
        if root is not None:
            Node.postorder_traversal(root.left)
            Node.postorder_traversal(root.right)
            print(root.key)


root = None
root = Node.insert(root, 10)
root = Node.insert(root, 5)
root = Node.insert(root, 15)
root = Node.insert(root, 3)
root = Node.insert(root, 12)
root = Node.insert(root, 20)

if Node.search(root, 15):
    print("Nilai 15 ditemukan dalam pohon")
else:
    print("Nilai 15 tidak ditemukan dalam pohon")

print("Preorder traversal:")
Node.preorder_traversal(root)

print("Inorder traversal:")
Node.inorder_traversal(root)

print("Postorder traversal:")
Node.postorder_traversal(root)
