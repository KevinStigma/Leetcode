class Solution(object):
	def lengthOfLongestSubstring(self, s):
		if len(s)==0:
			return 0
		begin=0
		end=0
		max_len=0
		visited={}
		for i in range(len(s)):
			visited[s[i]]=0
		while begin<=end and end<len(s):
			if visited[s[end]]==0:
				visited[s[end]]=1
				max_len=max(max_len,end-begin+1)
				end=end+1
			else:
				visited[s[begin]]=visited[s[begin]]-1
				begin=begin+1
		return max_len
s=Solution()
print s.lengthOfLongestSubstring('pwwkew')