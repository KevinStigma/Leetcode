class Solution(object):
    def findTheDifference(self, s, t):
		s1=list(s)
		t1=list(t)
		s1.sort()
		t1.sort()
		for i in range(len(s1)):
			if s1[i]!=t1[i]:
				return t1[i]
		return t1[-1]
		
s=Solution()
print s.findTheDifference('abcd','abcde')