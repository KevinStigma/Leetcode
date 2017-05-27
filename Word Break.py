class Solution(object):
	def wordBreak(self, s, wordDict):
		map={}
		for word in wordDict:
			if not(word[-1] in map):
				map[word[-1]]=[word]
			else:
				map[word[-1]].append(word)
		dp=[False]*len(s)
		for i in range(len(s)):
			if s[i] in map:
				words=map[s[i]]
				for word in words:
					prev=0
					if len(word)-1<=i:
						prev=i-len(word)+1
					else:
						continue
					if s[prev:i+1]==word and (prev==0 or dp[prev-1]==True):
						dp[i]=True
						prev=i+1
						break
		return dp[-1]
s=Solution()
print s.wordBreak("aaaaaaa",["aaaa","aaa"])