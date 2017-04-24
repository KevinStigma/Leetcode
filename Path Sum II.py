# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.results=[]
	def preOrder(self,root,number,sum,path):
		if root==None:
			return
		number=number+root.val
		path.append(root.val)
		if root.left==None and root.right==None:
			if number==sum:
				self.results.append(path[:])
		self.preOrder(root.left,number,sum,path)
		self.preOrder(root.right,number,sum,path)
		path.pop()
		
	def pathSum(self, root, sum):
		self.results=[]
		if root==None:
			return self.results
		self.preOrder(root,0,sum,[])
		return self.results