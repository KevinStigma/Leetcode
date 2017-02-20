class Solution(object):
	def firstMissingPositive(self, nums):
		for i in range(len(nums)):
			while nums[i]>0 and nums[i]>i+1 and nums[i]<=len(nums):
				d=nums[i]
				if nums[i]==nums[d-1]:
					break
				nums[i]=nums[d-1]
				nums[d-1]=d
			if nums[i]>0 and nums[i]<i+1:
				d=nums[i]
				nums[i]=-1
				nums[d-1]=d
		for i in range(len(nums)):
			if nums[i]!=i+1:
				return i+1
		return len(nums)+1
	def firstMissingPositive2(self, nums):#more simple solution
		for i in range(len(nums)):
			while nums[i]>0 and nums[i]<=len(nums) and nums[i]!=nums[nums[i]-1]:
				nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
		for i in range(len(nums)):
			if nums[i]!=i+1:
				return i+1
		return len(nums)+1
				
s=Solution()
print s.firstMissingPositive2([0,1,2])