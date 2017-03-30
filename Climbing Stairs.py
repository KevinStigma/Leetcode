class Solution(object):
	def climbStairs(self, n):
		if n==1:
			return 1
		elif n==2:
			return 2
		p=[1,2]
		for i in range(2,n):
			p.append(p[i-1]+p[i-2])
		return p[n-1]
s=Solution()
print s.climbStairs(3)
		