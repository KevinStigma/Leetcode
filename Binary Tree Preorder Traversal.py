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
	
	def preOrderNoRecur(self,root):
		stack=[]
		list=[]
		if root==None:
			return list
		p=root
		while(len(stack)!=0 or p!=None):
			while p!=None:
				list.append(p.val)
				stack.append(p)
				p=p.left
			if len(stack):
				p=stack[-1]
				stack.pop()
				p=p.right
		return list
		
	def preOrderNoRecur2(self,root):
		stack=[]
		list=[]
		if root==None:
			return list
		p=root
		stack.append(p)
		while len(stack):
			p=stack[-1]
			stack.pop()
			list.append(p.val)
			if p.right:
				stack.append(p.right)
			if p.left:
				stack.append(p.left)
		return list
	
	def preorderTraversal(self, root):
		if root==None:
			return []
		list=[]
		self.preOrder(root,list)
		return list