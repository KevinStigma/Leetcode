class Solution(object):
	def sortColors(self, nums):
		#counting sort
		C=[0]*3
		B=[0]*len(nums)
		for i in range(len(nums)):
			C[nums[i]]=C[nums[i]]+1
		for i in range(len(C)-1):
			C[i+1]=C[i]+C[i+1]
		for i in range(len(nums)):
			B[C[nums[i]]-1]=nums[i]
			C[nums[i]]=C[nums[i]]-1
		for i in range(len(nums)):
			nums[i]=B[i]
s=Solution()
s.sortColors([0,0,2,1,2,0])