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

	def __repr__(self):
		return f"{self.key}"

a = BinarySearchTree(10)
a.insert(5)
a.insert(30)

print(a.left,a.key,a.right)