class Solution(object):
	def twoSum(self, nums, target):
		hashMap={}
		for i in range(len(nums)):		
			n=target-nums[i]
			if n in hashMap:
				j=hashMap[n]
				if i<j:
					return [i,j]
				else:
					return [j,i]
			hashMap[nums[i]]=i
	def twoSum2(self,nums,target):
		sorted_index=sorted(range(len(nums)), key=lambda k: nums[k])
		nums.sort()
		low=0
		high=len(nums)-1
		while low<high:
			if nums[low]+nums[high]==target:
				return [sorted_index[low],sorted_index[high]]
			elif nums[low]+nums[high]>target:
				high=high-1
			else:
				low=low+1
				
solution=Solution()
print solution.twoSum2([3,2,4],6)