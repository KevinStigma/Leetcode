class Solution(object):
	def thirdMax(self, nums):
		max_num=nums[0]
		for num in nums:
			max_num=max(max_num,num)
		second_num=None
		for i in range(len(nums)):
			if nums[i]!=max_num and (second_num==None or second_num<nums[i]):
				second_num=nums[i]
		third_num=None
		for i in range(len(nums)):
			if nums[i]!=max_num and nums[i]!=second_num and (third_num==None or third_num<nums[i]):
				third_num=nums[i]
		if third_num==None:
			return max_num
		return third_num
s=Solution()
print s.thirdMax([2,2,3,1])