def isPalindrome(cur_str):
	if len(cur_str)==0:
		return False
	begin=0
	end=len(cur_str)-1
	while begin<end:
		if cur_str[begin]!=cur_str[end]:
			return False
		begin=begin+1
		end=end-1
	return True
	
class Solution(object):
	def __init__(self):
		self.results=[]
	def backTracing(self,cur_str,cur_res):
		for i in range(len(cur_str)):
			tmp_str=cur_str[0:i+1]
			if isPalindrome(tmp_str):
				cur_res.append(tmp_str)
				if i!=len(cur_str)-1:
					self.backTracing(cur_str[i+1:],cur_res)
				else:
					self.results.append(cur_res[:])
				cur_res.pop()
	def partition(self, s):
		self.results=[]
		if len(s)==0:
			return []
		if len(s)==1:
			return [[s[0]]]
		self.backTracing(s,[])
		return self.results

s=Solution()
print s.partition("aab")