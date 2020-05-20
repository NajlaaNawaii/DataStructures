# Node Class
class Node:
    # Default Constructor
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # A utility function to insert a new node with given key in BST
    def insert(self, key):
      
      # If the tree is empty, return a new node
      if self is None:
        self = Node(key)
        return
      
      # Otherwise, recur down the tree
      if key < self.key:
        if self.left:
          self.left.insert(key)
        else:
          self.left = Node(key)
          return      
      else:
        if self.right:
          self.right.insert(key)
        else:
          self.right = Node(key)
          return
        
# BST Class    
class binarySearchTree:
    def __init__(self, key):
        self.root = Node(key)
    
    def insert(self, key):
      self.root.insert(key)
      
# inorder tree traversal 
def inorder(root): 
  if root: 
    inorder(root.left) 
    print(root.key) 
    inorder(root.right) 
  


BST = binarySearchTree(6)

BST.insert(3)
BST.insert(9)
BST.insert(1)
BST.insert(5)
BST.insert(7)
BST.insert(11)


inorder(BST.root)