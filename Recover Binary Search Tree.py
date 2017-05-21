# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.values=[]
		self.pointers=[]
		
	def inOrder(self,root):
		if root!=None:
			self.inOrder(root.left)
			self.values.append(root.val)
			self.pointers.append(root)
			self.inOrder(root.right)
		
	def recoverTree(self, root):
		self.values=[]
		self.pointers=[]
		if root==None:
			return
		self.inOrder(root)
		ind1=ind2=0
		for i in range(ind1,len(self.values)-1):
			if self.values[i]>self.values[i+1]:
				ind1=i
				break
		for i in range(ind1+1,len(self.values)):
			if self.values[i]>self.values[ind1]:
				ind2=i-1
				break
			elif i==len(self.values)-1:
				ind2=len(self.values)-1
				break
		tmp=self.pointers[ind1].val
		self.pointers[ind1].val=self.pointers[ind2].val
		self.pointers[ind2].val=tmp

s=Solution()
s.recoverTree()