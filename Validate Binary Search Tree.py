# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.nums=[]
	
	def inOrder(self,root):
		if root!=None:
			self.inOrder(root.left)
			self.nums.append(root.val)
			self.inOrder(root.right)
		
	def isValidBST(self, root):
		self.nums=[]
		if root==None:
			return True
		if root.left==None and root.right==None:
			return True
		self.inOrder(root)
		sorted_nums=self.nums[:]
		sorted_nums.sort()
		for i in range(len(sorted_nums)):
			if sorted_nums[i]!=self.nums[i]:
				return False
			if i!=0 and sorted_nums[i]==sorted_nums[i-1]:
				return False
		return True