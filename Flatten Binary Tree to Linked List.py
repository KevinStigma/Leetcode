# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def flattenTree(self,root):
		if root==None:
			return None
		tail=root
		l_root=root.left
		r_root=root.right
		l_tail=self.flattenTree(root.left)	
		r_tail=self.flattenTree(root.right)
		root.left=None
		root.right=None
		if l_tail!=None:
			tail.right=l_root
			tail=l_tail
		if r_tail!=None:
			tail.right=r_root
			tail=r_tail
		return tail
		
	def flatten(self, root):
		if root==None:
			return None
		self.flattenTree(root)
