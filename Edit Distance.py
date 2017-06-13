class Solution(object):
	#each operation must be added in the end of current substring
	def minDistance(self, word1, word2):
		l1=len(word1)
		l2=len(word2)
		dp=[[-1]*(l2+1) for i in range(l1+1)]
		dp[0][0]=0
		for i in range(1,l2+1):
			dp[0][i]=i
		for i in range(1,l1+1):
			dp[i][0]=i
		for i in range(1,l1+1):
			for j in range(1,l2+1):
				v1=dp[i][j-1]+1
				v2=dp[i-1][j]+1
				v3=dp[i-1][j-1]
				if word1[i-1]!=word2[j-1]:
					v3=v3+1
				dp[i][j]=min(min(v1,v2),v3)
		return dp[l1][l2]
s=Solution()
print s.minDistance("ab","a")