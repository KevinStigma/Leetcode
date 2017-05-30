class Solution(object):
	def __init__(self):
		self.results=[]
	def DFS(self,dp,wordDict,cur_id,cur_list):
		if cur_id<0 or len(dp[cur_id])==0:
			return 
		list=dp[cur_id]
		for i in range(len(list)):
			ind=list[i]
			cur_list.append(ind)
			if cur_id-len(wordDict[ind])+1==0:
				res=''
				for j in range(len(cur_list)-1,-1,-1):
					res=res+wordDict[cur_list[j]]
					if j!=0:
						res=res+' '
				self.results.append(res)
			else:	
				self.DFS(dp,wordDict,cur_id-len(wordDict[ind]),cur_list)
			cur_list.pop()
			
	def wordBreak(self, s, wordDict):
		if len(s)==0 or len(wordDict)==0:
			return []
		maps={}
		self.results=[]
		for i in range(len(wordDict)):
			word=wordDict[i]
			if word[-1] in maps:
				maps[word[-1]].append(i)
			else:
				maps[word[-1]]=[i]
		dp=[[] for i in range(len(s))]
		for i in range(len(s)):
			if s[i] in maps:
				word_inds=maps[s[i]]
				for word_ind in word_inds:
					prev=i-len(wordDict[word_ind])+1
					if prev<0:
						continue
					if s[prev:i+1]==wordDict[word_ind] and (prev==0 or len(dp[prev-1])>0):
						dp[i].append(word_ind)
		self.DFS(dp,wordDict,len(s)-1,[])
		return self.results
		
s=Solution()
print s.wordBreak('catsanddog',["cat", "cats", "and", "sand", "dog"])