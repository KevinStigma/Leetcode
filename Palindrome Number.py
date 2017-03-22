class Solution:
	def isPalindrome(self, x):
		o = x
		ret = 0
		if x < 0:
			return False
		while(x!=0):
			ret = ret*10+x%10
			x = x/10
		return ret == o