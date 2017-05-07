# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.left_list=[]
		self.right_list=[]
	def preOrder(self,root,flag):
		if root!=None:
			if flag==1:
				self.left_list.append(root.val)
				self.preOrder(root.left,flag)
				self.preOrder(root.right,flag)
			else:
				self.right_list.append(root.val)
				self.preOrder(root.right,flag)
				self.preOrder(root.left,flag)
		else:
			if flag==1:
				self.left_list.append(0)
			else:
				self.right_list.append(0)
	def isSymmetric(self, root):
		self.left_list=[]
		self.right_list=[]
		if root==None:
			return True
		if root.left==None and root.right==None:
			return True
		self.preOrder(root.left,1)
		self.preOrder(root.right,2)
		if len(self.left_list)!=len(self.right_list):
			return False
		for i in range(len(self.left_list)):
			if self.left_list[i]!=self.right_list[i]:
				return False
		return True