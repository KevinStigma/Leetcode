class Solution(object):
	def canJump(self, nums):
		i=0
		while i<len(nums):
			if i+nums[i]>=len(nums)-1:
				return True
			if nums[i]==0:
				return False
			max_jump=0
			ind=-1
			for j in range(i+1,i+nums[i]+1):
				if j>len(nums)-1:
					break
				if max_jump<(j-i+nums[j]):
					max_jump=(j-i+nums[j])
					ind=j
			i=ind
		return False
s=Solution()
print s.canJump([3,2,1,0,4])