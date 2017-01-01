class Solution(object):
	def longestCommonPrefix(self, strs):
		if len(strs)==0:
			return ""
		elif len(strs)==1:
			return strs[0]
		l=len(strs[0])
		for i in range(0,l):
			for j in range(1,len(strs)):
				if len(strs[j])<i+1:
					return strs[0][:i]
				elif strs[j][i]!=strs[0][i]:
					return strs[0][:i]
		return strs[0]
			
s=Solution()
print s.longestCommonPrefix(['abc','ab','abe','abcde'])