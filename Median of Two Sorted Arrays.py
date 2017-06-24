class Solution(object):
	def getMidVal(self,nums):
		mid=(0+len(nums)-1)/2
		if len(nums)%2==0:
			return float(nums[mid]+nums[mid+1])/2.0
		else:
			return float(nums[mid])
		
		
	def findMedianSortedArrays(self, nums1, nums2):
		if len(nums1)==0 and len(nums2)==0:
			return 0.0
		if len(nums1)==0:
			return self.getMidVal(nums2)
		if len(nums2)==0:
			return self.getMidVal(nums1)
		nums=[0]*(len(nums1)+len(nums2))
		ind1=0
		ind2=0
		ind=0
		while ind1!=len(nums1) and ind2!=len(nums2):
			if nums1[ind1]<nums2[ind2]:
				nums[ind]=nums1[ind1]
				ind1=ind1+1
				ind=ind+1
			else:
				nums[ind]=nums2[ind2]
				ind2=ind2+1
				ind=ind+1
		if ind1<len(nums1):
			while ind1<len(nums1):
				nums[ind]=nums1[ind1]
				ind=ind+1
				ind1=ind1+1
		else:
			while ind2<len(nums2):
				nums[ind]=nums2[ind2]
				ind=ind+1
				ind2=ind2+1
		return self.getMidVal(nums)
			
s=Solution()
print s.findMedianSortedArrays([1,2],[3,4])