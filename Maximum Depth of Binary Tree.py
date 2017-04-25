# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.max_depth=0
	def preOrder(self,root,depth):
		if root!=None:
			if root.left==None and root.right==None:
				if depth>self.max_depth:
					self.max_depth=depth
			else:
				self.preOrder(root.left,depth+1)
				self.preOrder(root.right,depth+1)
	def maxDepth(self, root):
		if root==None:
			return self.max_depth
		self.preOrder(root,1)
		return self.max_depth
		
		