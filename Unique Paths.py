class Solution(object):
	def uniquePaths(self, m, n):
		if m==0 and n==0:
			return 0
		if m==1 or n==1:
			return 1
		maze=[[0]*n for i in range(m)]
		for i in range(m):
			maze[i][0]=1
		for i in range(n):
			maze[0][i]=1
		for i in range(1,m):
			for j in range(1,n):
				maze[i][j]=maze[i-1][j]+maze[i][j-1]
		return maze[m-1][n-1]	
		
s=Solution()
print s.uniquePaths(2,3)