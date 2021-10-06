class BinarySearchTree:
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None

	def insert(self,value):
		if self.key is None:
			self.key = value
			return
		if self.key == value:
			return
		if value < self.key:
			if self.left:
				self.left.insert(value)
			else:
				self.left = BinarySearchTree(value)
		else:
			if self.right:
				self.right.insert(value)
			else:
				self.right = BinarySearchTree(value)

	def search(self,value):
		if self.key == value:
			print(f"Node {value} exists.")
			return
		if value < self.key:
			if self.left:
				self.left.search(value)
			else:
				print(f"Node {value} not found.")
		else:
			if self.right:
				self.right.search(value)
			else:
				print(f"Node {value} not found.")
	#Traversal
	def preorder(self):
		print(self.key)
		if self.left:
			self.left.preorder()
		if self.right:
			self.right.preorder()

	def inorder(self):
		
		if self.left:
			self.left.inorder()

		print(self.key)

		if self.right:
			self.right.inorder()

	def __repr__(self):	
		return f"{self.key}"

a = BinarySearchTree(21)
for val in [10,30,5,12,25,100,3,7]:
	a.insert(val)

#for val in [1,5,2,56,12,56,121,-1]:
#	a.search(val)

#a.preorder()
a.inorder()