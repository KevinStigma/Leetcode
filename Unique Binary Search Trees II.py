# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.results=[]
	def constructTrees(self,nums,begin,end):
		results=[]
		if begin>end:
			return results
		for i in range(begin,end+1):
			left_trees=self.constructTrees(nums,begin,i-1)
			right_trees=self.constructTrees(nums,i+1,end)
			if len(left_trees)==0 and len(right_trees)==0:
				root=TreeNode(nums[i])
				results.append(root)
			elif len(left_trees)==0:
				for right in right_trees:
					root=TreeNode(nums[i])
					root.right=right
					results.append(root)
			elif len(right_trees)==0:
				for left in left_trees:
					root=TreeNode(nums[i])
					root.left=left
					results.append(root)
			else:
				for left in left_trees:
					for right in right_trees:
						root=TreeNode(nums[i])
						root.left=left
						root.right=right
						results.append(root)
		return results
	def generateTrees(self, n):
		self.results=[]
		if n==0:
			return self.results
		nums=[i for i in range(1,n+1)]
		return self.constructTrees(nums,0,n-1)
		
s=Solution()
print s.generateTrees(1)