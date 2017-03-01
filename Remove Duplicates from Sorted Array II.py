class Solution(object):
	def removeDuplicates(self, nums):
		length=0
		count=0
		for i in range(len(nums)):
			if i>0 and nums[i]==nums[i-1]:
				count=count+1
				if count>=2:
					continue
				length=length+1
				continue
			count=0
			length=length+1
		i=1
		id=1
		count=0
		while i<len(nums):
			if nums[i]==nums[i-1]:
				count=count+1
				if count>=2:
					i=i+1
					continue
			else:
				count=0
			nums[id]=nums[i]
			id=id+1
			i=i+1
		return length
s=Solution()
print s.removeDuplicates([1,1,1,2,2,3])