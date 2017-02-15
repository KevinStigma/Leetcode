def BinarySearch(a, target,low,high): 
	while low <= high:
		mid = (low + high) // 2
		midVal = a[mid]
		
		if midVal < target:
			low = mid + 1
		elif midVal > target:
			high = mid - 1
		else:
			return mid
	return -1
	
class Solution(object):
	def search(self, nums, target):
		if len(nums)==0:
			return -1
		low=0
		high=len(nums)-1
		while nums[low]>nums[high]:
			mid=(low+high)//2
			if target==nums[mid]:
				return mid
			if nums[mid]>=nums[low]:
				if target>nums[high] and target<=nums[mid]:
					return BinarySearch(nums,target,low,mid)
				else:
					low=mid+1
			else:
				if target<nums[low] and target>=nums[mid]:
					return BinarySearch(nums,target,mid,high)
				else:
					high=mid-1
		return BinarySearch(nums,target,low,high)
		
s=Solution()
print s.search([1],0)