# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preOrder(self,root):
		if root!=None:
			num1=self.preOrder(root.left)
			num2=self.preOrder(root.right)
			if num1==-1 or num2==-1:
				return -1
			if abs(num1-num2)<=1:
				return max(1+num1,1+num2)
			else:
				return -1
		return 0
	def isBalanced(self, root):
		if root==None:
			return True
		if self.preOrder(root)!=-1:
			return True
		return False