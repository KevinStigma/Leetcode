# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	
class Solution(object):
	def __init__(self):
		self.nums=[]
	def preOrder(self,root,number):
		if root!=None:
			num=number+root.val
			if root.left==None and root.right==None:
				self.nums.append(num)
			else:
				self.preOrder(root.left,num*10)
				self.preOrder(root.right,num*10)
	def sumNumbers(self, root):
		self.nums=[]
		if root==None:
			return 0
		self.preOrder(root,0)
		sum=0
		for n in self.nums:
			sum=sum+n
		return sum
node=TreeNode(1)
child=TreeNode(0)
node.left=child
s=Solution()
print s.sumNumbers(node)
			