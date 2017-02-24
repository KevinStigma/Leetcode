class Solution(object):
	def __init__(self):
		self.triplets=[]
		
	def twoSum(self,nums,target,low,high):
		while low<high:
			if nums[low]+nums[high]==target:
				self.triplets.append([-target,nums[low],nums[high]])
				value=nums[low]
				low=low+1
				while low<len(nums) and value==nums[low]:
					low=low+1
				value=nums[high]
				high=high-1
				while high>=0 and nums[high]==value:
					high=high-1
			elif nums[low]+nums[high]>target:
				value=nums[high]
				high=high-1
				while high>=0 and nums[high]==value:
					high=high-1
			else:
				value=nums[low]
				low=low+1
				while low<len(nums) and value==nums[low]:
					low=low+1
		
	def threeSum(self, nums):
		self.triplets=[]
		nums.sort()
		for i in range(len(nums)):
			if i!=0 and nums[i]==nums[i-1]:
				continue
			if nums[i]>0:
				continue
			remainder=-nums[i]
			self.twoSum(nums,remainder,i+1,len(nums)-1)
		return self.triplets

s=Solution()
print s.threeSum([-1,0,1,2,-1,-4])
				