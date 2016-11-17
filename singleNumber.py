class Solution(object):
    def singleNumber(self, nums):
		dic={}
		for num in nums:
			if num in dic:
				dic[num]=2
			else:
				dic[num]=1
		for item in dic:
			if dic[item]==1:
				return item
			
solution = Solution()
solution.singleNumber([1])			