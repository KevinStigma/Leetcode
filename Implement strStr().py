class Solution(object):
	def strStr(self, haystack, needle):
		if needle=="":
			return 0
		if len(haystack)<len(needle):
			return -1
		return haystack.find(needle)
s=Solution()
print s.strStr("mississippi","issippi")