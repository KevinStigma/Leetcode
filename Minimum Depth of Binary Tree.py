# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.min_depth=0
	def preOrder(self,root,depth):
		if root!=None:
			if root.left==None and root.right==None:
				if self.min_depth==0 or self.min_depth>depth:
					self.min_depth=depth
			else:
				self.preOrder(root.left,depth+1)
				self.preOrder(root.right,depth+1)
	def minDepth(self, root):
		if root==None:
			return 0
		self.preOrder(root,1)
		return self.min_depth