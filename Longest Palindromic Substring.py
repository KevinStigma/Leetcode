class Solution(object):
	def longestPalindrome(self, s):
		longest_str=''
		for i in range(len(s)):
			low=i-1
			high=i+1
			while low>=0 and high<len(s):
				if s[low]!=s[high]:
					break
				low=low-1
				high=high+1
			if high-1-low>len(longest_str):
				longest_str=s[low+1:high]
			
			low=i-1
			high=i
			while low>=0 and high<len(s):
				if s[low]!=s[high]:
					break
				low=low-1
				high=high+1
			if low!=high-1:
				if high-1-low>len(longest_str):
					longest_str=s[low+1:high]
		return longest_str
s=Solution()
print s.longestPalindrome('bb')