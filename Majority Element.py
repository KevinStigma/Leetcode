class Solution(object):
	def majorityElement(self, nums):
		if len(nums)==1 or len(nums)==2:
			return nums[0]
		nums.sort()
		flag=len(nums)/2
		count=1
		cur_num=nums[0]
		major_num=cur_num
		for i in range(1,len(nums)):
			if cur_num!=nums[i] and count<=flag:
				cur_num=nums[i]
				count=1
			elif cur_num!=nums[i] and count>flag:
				major_num=cur_num
				break
			else:
				count=count+1
			if i==len(nums)-1 and count>flag:
				major_num=cur_num
		return major_num
s=Solution()
print s.majorityElement([3,2,3])