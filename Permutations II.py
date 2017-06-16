class Solution(object):
	def __init__(self):
		self.results=[]
	def DFS(self,nums,visited,result,depth):
		if depth==len(nums):
			self.results.append(result[:])
			return
		for i in range(len(nums)):
			if i!=0 and nums[i]==nums[i-1]:
				if visited[i-1]==True and visited[i]==False:
					result.append(nums[i])
					visited[i]=True
					self.DFS(nums,visited,result,depth+1)
					result.pop()
					visited[i]=False
			elif visited[i]==False:
				result.append(nums[i])
				visited[i]=True
				self.DFS(nums,visited,result,depth+1)
				result.pop()
				visited[i]=False
	def permuteUnique(self, nums):
		self.results=[]
		if len(nums)==0:
			return self.results
		nums.sort()
		visited=[False]*len(nums)
		self.DFS(nums,visited,[],0)
		return self.results
s=Solution()
print s.permuteUnique([3,3,0,3])