class Solution(object):
	def merge(self, nums1, m, nums2, n):
		new_list=[]
		ind1=0
		ind2=0
		for i in range(m+n):
			if  ind1<m and ind2<n and nums1[ind1]<=nums2[ind2]:
				new_list.append(nums1[ind1])
				ind1=ind1+1
			elif ind1<m and ind2<n and nums1[ind1]>=nums2[ind2]:
				new_list.append(nums2[ind2])
				ind2=ind2+1
			elif ind1==m and ind2<n:
				new_list.append(nums2[ind2])
				ind2=ind2+1
			elif ind2==n and ind1<m:
				new_list.append(nums1[ind1])
				ind1=ind1+1
		for i in range(m+n):
			nums1[i]=new_list[i]
s=Solution()
s.merge([1,2,3,0,0,0],3,[2,5,6],3)