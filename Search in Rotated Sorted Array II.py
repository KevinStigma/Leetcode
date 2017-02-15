def BinarySearch(a, target,low,high): 
	while low <= high:
		mid = (low + high) // 2
		midVal = a[mid]
		
		if midVal < target:
			low = mid + 1
		elif midVal > target:
			high = mid - 1
		else:
			return True
	return False
	
class Solution(object):
	def search(self, nums, target):
		if len(nums)==0:
			return False
		low=0
		high=len(nums)-1
		while nums[low]>=nums[high]:
			#We should deal with the case that the value of end and start is the same
			if nums[low]==nums[high]:
				value=nums[low]
				if value==target:
					return True
				l=low
				h=high
				while nums[l]==value:
					l=l+1
					if l>=high:
						return False
				while nums[h]==value:
					h=h-1
					if h<=low:
						return False
				low=l
				high=h
				continue
			print str(low)+' '+str(high)	
			mid=(low+high)//2
			if target==nums[mid]:
				return True
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
print s.search([1,3,1,1,1],3)