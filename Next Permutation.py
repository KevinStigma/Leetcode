class Solution(object):
	def nextPermutation(self, nums):
		l=len(nums)
		ind=l-1
		for i in range(l):
			is_decrease=True
			for j in range(i+1,l):
				if nums[j]>nums[j-1]:
					is_decrease=False
					break
			if is_decrease==True:
				ind=i
				break
		if ind>0:
			num=nums[ind-1]
			large_ind=-1
			for i in range(ind,l):
				if nums[i]<=num:
					large_ind=i-1
					break
			tmp=nums[ind-1]
			nums[ind-1]=nums[large_ind]
			nums[large_ind]=tmp
			tmp_list=nums[ind:]
			tmp_list.sort()
			nums[ind:]=tmp_list[:]
		else:
			nums.sort()
		print nums
s=Solution()
s.nextPermutation([5,4,3,2,1])