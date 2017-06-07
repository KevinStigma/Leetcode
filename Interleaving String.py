class Solution(object):
	def isInterleave(self, s1, s2, s3):
		n1=len(s1)
		n2=len(s2)
		if n1==0 and n2==0 and len(s3)==0:
			return True
		if len(s3)!=n1+n2:
			return False
		dp=[[False]*(n2+1) for i in range(n1+1)]
		dp[0][0]=True
		for i in range(1,n1+1):
			if s3[i-1]!=s1[i-1]:
				break
			dp[i][0]=True
		for i in range(1,n2+1):
			if s3[i-1]!=s2[i-1]:
				break
			dp[0][i]=True
		for i in range(1,n1+1):	
			for j in range(1,n2+1):
				if (dp[i-1][j]==True and s3[i-1+j]==s1[i-1]) or (dp[i][j-1]==True and s3[i-1+j]==s2[j-1]):
					dp[i][j]=True
		return dp[n1][n2]
s=Solution()
print s.isInterleave("aabcc","dbbca","aadbbbaccc")