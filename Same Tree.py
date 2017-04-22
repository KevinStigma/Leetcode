# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preOrder(self, p, q):
		if (p==None and q!=None) or (q==None and p!=None):
			return False
		if p==None and q==None:
			return True
		if p.val!=q.val:
			return False
		if self.preOrder(p.left,q.left) and self.preOrder(p.right,q.right):
			return True
		return False
		
	def isSameTree(self, p, q):
		return self.preOrder(p,q)