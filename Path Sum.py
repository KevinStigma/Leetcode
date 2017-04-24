# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preOrder(self,root,number,sum):
		if root==None:
			return False
		number=number+root.val
		if root.left==None and root.right==None:
			if number==sum:
				return True
			return False
		if self.preOrder(root.left,number,sum) or self.preOrder(root.right,number,sum):
			return True
		return False
	def hasPathSum(self, root, sum):
		if root==None:
			return False
		return self.preOrder(root,0,sum)