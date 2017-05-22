class Solution(object):
	def subsets(self, nums):
		n=len(nums)
		subsets=[]
		for i in range(1<<n):
			set=[]
			num=i
			for j in range(n):
				if(num&(1<<j)):
					set.append(nums[j])
			subsets.append(set)
		return subsets
s=Solution()
print s.subsets([1,2,3])