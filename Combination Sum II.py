class Solution(object):
	def __init__(self):
		self.combinations=[]
		self.sum=0
	def DFS(self,begin,combin,candidates,target):
		if self.sum>=target:
			if self.sum==target:
				self.combinations.append(combin[:])
			return
		if begin>=len(candidates):
			return
		#because the items of candidates will have repeated num, we can't allow
		#the same items be used repeatedly in the identical recursive layer
		used_num=None
		for i in range(begin,len(candidates)):
			if candidates[i]==used:
				continue
			self.sum=self.sum+candidates[i]
			combin.append(candidates[i])
			self.DFS(i+1,combin,candidates,target)
			self.sum=self.sum-candidates[i]
			combin.pop()
			used_num=candidates[i]
			
	def combinationSum2(self, candidates, target):
		self.combinations=[]
		combin=[]
		self.sum=0
		candidates.sort()
		self.DFS(0,combin,candidates,target)
		return self.combinations
s=Solution()
print s.combinationSum2([10, 1, 2, 7, 6, 1, 5],8)