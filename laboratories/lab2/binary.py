class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def PrintTree(self):
    if self is not None:
      print(self.data)
      if self.left is not None: 
        self.left.PrintTree()
      if self.right is not None:  
        self.right.PrintTree()
  def get_val(self):
    return self.data

  def binary_search(self, value):
    print(self.data) 
    if self.data == value:
      print(f"Found: {self.data}")
    elif value < self.data:
      if self.left is not None:
        self.left.binary_search(value)
      else:
        print(f"{value} not found.")
    else:  
      if self.right is not None:
        self.right.binary_search(value)
      else:
        print(f"{value} not found.")

def insert(node, value):
  if value < node.data:
    if node.left is None:
      node.left = Node(value)
    else:
      insert(node.left, value)
  else:
    if node.right is None:
      node.right = Node(value)
    else:
      insert(node.right, value)

def create_tree(nums):
    if not nums:
        return None
    root = Node(nums[0])
    for num in nums[1:]:
        insert(root, num)
    return root


root = Node(5)
root.left = Node(3)
root.left.right = Node(4)
root.right = Node(8)
root.right.left = Node(7)

x = create_tree([1, 2, 5, 3, 9, 11])

x.binary_search(5)
root.binary_search(6)
root.binary_search(7)
