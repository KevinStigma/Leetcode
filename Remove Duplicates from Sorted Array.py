class Solution(object):
	def removeDuplicates(self, nums):
		if nums==[]:
			return 0
		length=0
		value=1000000
		max_value=1000000
		for i in range(len(nums)):
			if i>0 and nums[i]==nums[i-1]:
				continue
			length=length+1
			
		value=nums[0]
		for i in range(len(nums)-1):
			if nums[i+1]==value:
				nums[i+1]=max_value
			else:
				value=nums[i+1]
		nums.sort()
		return length
s=Solution()
print s.removeDuplicates([1,1,1,2])