import os
class Solution(object):
	def getKthNum(self,k,nums1,nums2,begin1,begin2):
		if len(nums1)<=begin1:
			return nums2[begin2+k-1]
		elif len(nums2)<=begin2:
			return nums1[begin1+k-1]
		elif k==1:
			return min(nums1[begin1],nums2[begin2])
		k1=k/2
		k2=k-k/2
		if len(nums1)-begin1<k1:
			k1=len(nums1)-begin1
			k2=k-k1
		elif len(nums2)-begin2<k2:
			k2=len(nums2)-begin2
			k1=k-k2
		if nums1[begin1+k1-1]==nums2[begin2+k2-1]:
			return nums1[begin1+k1-1]
		elif nums1[begin1+k1-1]<nums2[begin2+k2-1]:
			return self.getKthNum(k-k1,nums1,nums2,begin1+k1,begin2)
		else:
			return self.getKthNum(k-k2,nums1,nums2,begin1,begin2+k2)
			
	def findMedianSortedArrays(self, nums1, nums2):
		mid=0
		if (len(nums1)+len(nums2))%2==0:
			mid=(len(nums1)+len(nums2))/2
			return (float(self.getKthNum(mid,nums1,nums2,0,0))+float(self.getKthNum(mid+1,nums1,nums2,0,0)))*0.5
		else:
			mid=(len(nums1)+len(nums2))/2+1
			return float(self.getKthNum(mid,nums1,nums2,0,0))
s=Solution()
print s.findMedianSortedArrays([1,3],[2])