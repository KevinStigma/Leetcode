class Solution(object):
	def numDistinct(self, s, t):
		if len(s)==0 or len(t)==0:
			return 0
		dp=[[0]*len(t) for i in range(len(s))]
		if s[0]==t[0]:
			dp[0][0]=1
		for i in range(1,len(s)):
			dp[i][0]=dp[i-1][0]
			if s[i]==t[0]:
				dp[i][0]=dp[i][0]+1
		for i in range(1,len(s)):
			for j in range(1,len(t)):
				if j>i:
					break
				dp[i][j]=dp[i-1][j]
				if s[i]==t[j]:
					dp[i][j]=dp[i][j]+dp[i-1][j-1]
		return dp[len(s)-1][len(t)-1]

s=Solution()
print s.numDistinct("rabbbit","rabbit")
