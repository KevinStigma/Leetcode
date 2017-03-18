class Solution(object):
	def maxSubArray(self, nums):
		sum=[0]*len(nums)
		sum[0]=nums[0]
		max_sum=nums[0]
		for i in range(1,len(nums)):
			if nums[i]>sum[i-1]+nums[i]:
				sum[i]=nums[i]
			else:
				sum[i]=sum[i-1]+nums[i]
			max_sum=max(max_sum,sum[i])
		return max_sum
		
s=Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])