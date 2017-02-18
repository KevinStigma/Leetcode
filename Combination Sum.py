class Solution(object):
	def __init__(self):
		self.combinations=[]
		self.sum=0
	def DFS(self,combin,begin,candidates,target):
		if self.sum>=target:
			if self.sum==target:
				self.combinations.append(combin[:])
			return 
		for i in range(begin,len(candidates)):
			self.sum=self.sum+candidates[i]
			combin.append(candidates[i])
			self.DFS(combin,i,candidates,target)
			self.sum=self.sum-candidates[i]
			combin.pop()
		
	def combinationSum(self, candidates, target):
		self.combinations=[]
		self.sum=0
		combin=[]
		self.DFS(combin,0,candidates,target)
		return self.combinations
		
s=Solution()
print s.combinationSum([2,3,6,7],7)