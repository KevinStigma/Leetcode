# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def rebuild(self,root,nums,begin,end):
		if root:
			mid=(begin+end)/2
			root.val=nums[mid]
			if mid>begin:
				root.left=TreeNode(0)
				self.rebuild(root.left,nums,begin,mid-1)
			if mid<end:
				root.right=TreeNode(0)
				self.rebuild(root.right,nums,mid+1,end)
		
	def sortedArrayToBST(self, nums):
		if len(nums)==0:
			return None
		root=TreeNode(0)
		self.rebuild(root,nums,0,len(nums)-1)
		return root
		