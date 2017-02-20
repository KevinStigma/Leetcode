class Solution(object):
	def generateMatrix(self, n):
		if n==0:
			return []
		matrix=[[0]*n for i in range(n)]
		count=1
		row=0
		col=0
		dir=4
		while count<=n*n:
			if dir==4:
				for i in range(col,len(matrix[0])):
					if matrix[row][i]!=0:
						break
					col=i
					matrix[row][col]=count
					count=count+1
				row=row+1
				dir=2
			elif dir==2:
				for i in range(row,len(matrix)):
					if matrix[i][col]!=0:
						break
					row=i
					matrix[row][col]=count
					count=count+1
				col=col-1
				dir=3
			elif dir==3:
				for i in range(col,-1,-1):
					if matrix[row][i]!=0:
						break
					col=i
					matrix[row][col]=count
					count=count+1
				row=row-1
				dir=1
			elif dir==1:
				for i in range(row,-1,-1):
					if matrix[i][col]!=0:
						break
					row=i
					matrix[row][col]=count
					count=count+1
				col=col+1
				dir=4
		return matrix
s=Solution()
print s.generateMatrix(1)