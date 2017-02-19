class Solution(object):
	def hammingDistance(self, x, y):
		result=x^y
		count=0
		while result>0:
			if result%2==1:
				count=count+1
			result=int(result/2)
		return count
s=Solution()
print s.hammingDistance(1,4)