class Solution(object):
	def minCut(self, s):
		if len(s)==0 or len(s)==1:
			return 0
			
		# dp[i][j] is to check s[i:j+1] is palindrome
		dp=[[0]*len(s) for i in range(len(s))]
		for i in range(len(s)):
			dp[i][i]=1
			if i!=len(s)-1 and s[i+1]==s[i]:
				dp[i][i+1]=1
				
		for i in range(len(s)-1,-1,-1):
			for j in range(i+2,len(s)):
				if dp[i+1][j-1]==1 and s[i]==s[j]:
					dp[i][j]=1
		
		count=[0]*len(s)
		for i in range(1,len(s)):
			min_num=count[i-1]+1
			for j in range(0,i):
				if dp[j][i]==1:
					if j==0:
						min_num=0
						break
					else:	
						min_num=min(count[j-1]+1,min_num)
			count[i]=min_num
		return count[-1]
s=Solution()
print s.minCut('abcccb')
			