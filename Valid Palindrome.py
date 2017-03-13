class Solution(object):
	def isPalindrome(self, s):
		if s=='':
			return True
		valid_str=[]
		for char in s:
			if char.isdigit() or char.isalpha():
				valid_str.append(char.lower())
		low=0
		high=len(valid_str)-1
		while low<high:
			if valid_str[low]!=valid_str[high]:
				return False
			low=low+1
			high=high-1
		return True
s=Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
		