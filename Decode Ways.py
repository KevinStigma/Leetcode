class Solution(object):
	def numDecodings(self, s):
		if len(s)==0 or s[0]=='0':
			return 0
		dp=[0]*len(s)
		dp[0]=1
		for i in range(1,len(s)):
			sum=0
			if s[i]!='0':
				sum=dp[i-1]
			num=int(s[i-1:i+1])
			if num<=26 and num>=10:
				if i==1:
					sum=sum+1
				else:
					sum=sum+dp[i-2]
			if sum==0:
				return 0
			dp[i]=sum
		return dp[-1]
s=Solution()
print s.numDecodings("100")