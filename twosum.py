class Solution(object):
    def twoSum(self, nums, target):
		hashMap={}
		for i in range(len(nums)):		
			n=target-nums[i]
			if n in hashMap:
				j=hashMap[n]
				if i<j:
					return [i,j]
				else:
					return [j,i]
			hashMap[nums[i]]=i
	
solution=Solution()
print solution.twoSum([3,2,4],6)