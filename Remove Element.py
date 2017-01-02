class Solution(object):
	def removeElement(self, nums, val):
		ind=0
		count=0
		end=len(nums)
		while ind!=end:
			if nums[ind]==val:
				for i in range(ind,end-1):
					nums[i]=nums[i+1]
				end=end-1
				continue
			ind=ind+1
		return end
		
s=Solution()
print s.removeElement([3,2,2,3,3],3)