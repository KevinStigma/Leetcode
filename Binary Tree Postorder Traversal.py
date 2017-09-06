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
	def postOrderNoRecur(self,root):
		stack=[]
		list=[]
		visited={}
		if root==None:
			return list
		p=root
		stack.append(p)
		while len(stack):
			if not (stack[-1] in visited):
				p=stack[-1]
				if p.right:
					stack.append(p.right)
				if p.left:
					stack.append(p.left)
				visited[p]=1
			else:
				list.append(stack[-1].val)
				stack.pop()
		return list
	def postorderTraversal(self, root):
		list=[]
		if root==None:
			return list
		self.postOrder(root,list)
		return list