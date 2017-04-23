# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def inOrder(self,root,list):
		if root!=None:
			self.inOrder(root.left,list)
			list.append(root.val)
			self.inOrder(root.right,list)		
		
	def inorderTraversal(self, root):
		list=[]
		if root==None:
			return list
		self.inOrder(root,list)
		return list