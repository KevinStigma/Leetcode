# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preOrder(self,root,list):
		if root!=None:
			list.append(root.val)
			self.preOrder(root.left,list)
			self.preOrder(root.right,list)
		
	def preorderTraversal(self, root):
		if root==None:
			return []
		list=[]
		self.preOrder(root,list)
		return list