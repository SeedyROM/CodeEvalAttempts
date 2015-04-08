class Node:
	def __init__(self, _value, _right=None, _left=None):
		self.right = _right
		self.left = _left
		self.value = _value

	def addChild(self, side, value):
		if side == 'right':
			self.right = Node(value)
		elif side == 'left':
			self.left = Node(value)

	def __int__(self):
		return int(self.value)

def print_tree_indented(tree, level=0):
    if tree == None: return
    print_tree_indented(tree.right, level+1)
    print '  ' * level + str(tree.value)
    print_tree_indented(tree.left, level+1)

tree = Node(1, Node(2,Node(4),Node(5)), Node(3,Node(5),Node(6)))

print_tree_indented(tree, 4)