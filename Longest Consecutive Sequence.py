class Solution(object):
	def longestConsecutive(self, nums):
		visited={}
		for i in range(len(nums)):
			if not (nums[i] in visited):
				visited[nums[i]]=False
		max_length=0
		for i in range(len(nums)):
			if visited[nums[i]]==False:
				length=1
				visited[nums[i]]=True
				j=nums[i]+1
				while (j in visited):
					visited[j]=True
					j=j+1
				length=length+j-nums[i]-1
				j=nums[i]-1
				while (j in visited):
					visited[j]=True
					j=j-1
				length=length+nums[i]-j-1
				max_length=max(max_length,length)
		return max_length
s=Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])