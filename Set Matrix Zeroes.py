class Solution(object):
	def setZeroes(self, matrix):
		m=len(matrix)
		n=len(matrix[0])
		row_info=[-1]*m
		col_info=[-1]*n
		for i in range(m):
			for j in range(n):
				if matrix[i][j]==0:
					row_info[i]=0
					col_info[j]=0
		for i in range(m):
			if row_info[i]==0:
				for j in range(n):
					matrix[i][j]=0
		for j in range(n):
			if col_info[j]==0:
				for i in range(m):
					matrix[i][j]=0
		
s=Solution()
s.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])						