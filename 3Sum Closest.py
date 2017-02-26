class Solution(object):
	def threeSumClosest(self, nums, target):
		nums.sort()
		closest_sum=nums[0]+nums[1]+nums[2]
		ind=[]
		for i in range(len(nums)-1):
			remainder=target-nums[i]
			low=i+1
			high=len(nums)-1
			while low<high:
				if nums[low]+nums[high]==remainder:
					return target
				elif nums[low]+nums[high]<remainder:
					if abs(target-closest_sum)>abs(remainder-nums[low]-nums[high]):
						#ind=[nums[i],nums[low],nums[high]]
						closest_sum=nums[i]+nums[low]+nums[high]
					low=low+1
				else:
					if abs(target-closest_sum)>abs(remainder-nums[low]-nums[high]):
						#ind=[nums[i],nums[low],nums[high]]
						closest_sum=nums[i]+nums[low]+nums[high]
					high=high-1
		return closest_sum
s=Solution()
print s.threeSumClosest([-1,2,1,-4],1)