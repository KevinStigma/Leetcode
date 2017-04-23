# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def postOrder(self,root,list):
		if root!=None:
			self.postOrder(root.left,list)
			self.postOrder(root.right,list)
			list.append(root.val)
		
	def postorderTraversal(self, root):
		list=[]
		if root==None:
			return list
		self.postOrder(root,list)
		return list