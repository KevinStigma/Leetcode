class Solution(object):
	def lengthOfLastWord(self, s):
		if len(s)==0:
			return 0
		for i in range(len(s)-1,-1,-1):
			if s[i]!=' ':
				break
			if i==0:
				return 0
				
		for j in range(i,-1,-1):
			if s[j]==' ':
				return i-j
		return i+1
s=Solution()
print s.lengthOfLastWord(' a  ')
			