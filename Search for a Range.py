def BinarySearch(a, target): 
	low = 0
	high = len(a) - 1
 
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
	def searchRange(self, nums, target):
		ind=BinarySearch(nums,target)
		if ind==-1:
			return [-1,-1]
		start=end=ind
		while nums[start]==target:
			start=start-1
			if start<0:
				break
		start=start+1
		while nums[end]==target:
			end=end+1
			if end==len(nums):
				break
		end=end-1
		return [start,end]
		
s=Solution()
print s.searchRange([1],1)