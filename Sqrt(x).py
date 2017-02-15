class Solution(object):
	def mySqrt(self, x):
		r=x
		last=r
		while abs(r*r-x)>0.0001:
			r=(r+x/r)*0.5
		return int(r)
s=Solution()
print s.mySqrt(5)