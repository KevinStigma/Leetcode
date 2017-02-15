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
	ind=low
	if ind>=len(a):
		ind=high
	if a[ind]>target:
		while ind>=0 and a[ind]>target:
			ind=ind-1
		return ind+1
	else:
		while ind<=len(a)-1 and a[ind]<target:
			ind=ind+1
		if ind==len(a):
			return ind
		return ind-1
	
class Solution(object):
	def searchInsert(self, nums, target):
		ind=BinarySearch(nums,target)
		return ind
		
s=Solution()
print s.searchInsert([1,3,5,6],7)