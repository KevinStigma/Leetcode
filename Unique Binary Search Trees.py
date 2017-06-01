class Solution(object):
	def numTrees(self, n):
		res=[0]*(n+1)
		res[0]=1
		res[1]=1
		for i in range(2,n+1):
			for j in range(1,i+1):
				left=j-1
				right=i-j
				res[i]=res[i]+res[left]*res[right]
		return res[n]
s=Solution()
print s.numTrees(4)