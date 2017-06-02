class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		if len(obstacleGrid)==0 or len(obstacleGrid[0])==0:
			return 0
		m=len(obstacleGrid)
		n=len(obstacleGrid[0])
		maze=[[0]*n for i in range(m)]
		if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
			return 0
		maze[0][0]=1
		for i in range(n):
			if obstacleGrid[0][i]==1:
				break
			else:
				maze[0][i]=1
		for i in range(m):
			if obstacleGrid[i][0]==1:
				break
			else:
				maze[i][0]=1
		for i in range(1,m):
			for j in range(1,n):
				s=0
				if obstacleGrid[i-1][j]==0:
					s=s+maze[i-1][j]
				if obstacleGrid[i][j-1]==0:
					s=s+maze[i][j-1]
				maze[i][j]=s
		return maze[m-1][n-1]
s=Solution()
print s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])