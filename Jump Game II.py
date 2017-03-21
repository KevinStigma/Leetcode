class Solution(object):
	def jump(self, nums):
		if(len(nums)==1):
			return 0
		curJump=0
		cur_ind=0
		while cur_ind<len(nums):
			max_length=0
			next_ind=cur_ind
			for i in range(cur_ind+1,cur_ind+1+nums[cur_ind]):
				if i>=len(nums)-1:
					return curJump+1
				if nums[i]==0:
					continue
				length=i-cur_ind+nums[i]
				if length>max_length:
					max_length=length
					next_ind=i
			cur_ind=next_ind
			curJump=curJump+1
		return curJump
s=Solution()
print s.jump([2,3,1,1,4])