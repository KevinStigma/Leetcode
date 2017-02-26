class Solution(object):
	def twoSum(self,nums,triplets,target,low,high,first_num):
		while low<high:
			if nums[low]+nums[high]==target:
				triplets.append([first_num,nums[low],nums[high]])
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
		
	def threeSum(self, nums,start,target):
		triplets=[]
		for i in range(start,len(nums)):
			if i>start and nums[i]==nums[i-1]:
				continue
			remainder=target-nums[i]
			self.twoSum(nums,triplets,remainder,i+1,len(nums)-1,nums[i])
		return triplets
	def fourSum(self, nums, target):
		quadruplets=[]
		nums.sort()
		for i in range(len(nums)-3):
			if i>0 and nums[i]==nums[i-1]:
				continue
			remainder=target-nums[i]
			triplets=self.threeSum(nums,i+1,remainder)
			if len(triplets)!=0:
				for result in triplets:
					quadruplets.append([nums[i],result[0],result[1],result[2]])
		return quadruplets
s=Solution()
print s.fourSum([5,5,3,5,1,-5,1,-2],4)