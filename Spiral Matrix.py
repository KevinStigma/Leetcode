class Solution(object):
	def spiralOrder(self, matrix):
		if len(matrix)==0:
			return []
		elif len(matrix)==1:
			return matrix[0]
		visited=[[False]*len(matrix[0]) for i in range(len(matrix))]
		row=0
		col=0
		dir=4 #up1 down2 left3 right4
		spiral_list=[]
		while visited[row][col]==False:
			if dir==4:
				for i in range(col,len(matrix[0])):
					if visited[row][i]==True:
						break
					col=i
					visited[row][col]=True
					spiral_list.append(matrix[row][col])
				row=row+1
				dir=2
			elif dir==2:
				
				for i in range(row,len(matrix)):
					if visited[i][col]==True:
						break
					row=i
					visited[row][col]=True
					spiral_list.append(matrix[row][col])
				col=col-1
				dir=3
			elif dir==3:
				for i in range(col,-1,-1):
					if visited[row][i]==True:
						break
					col=i
					visited[row][col]=True
					spiral_list.append(matrix[row][col])
				row=row-1
				dir=1
			elif dir==1:
				for i in range(row,-1,-1):
					if visited[i][col]==True:
						break
					row=i
					visited[row][col]=True
					spiral_list.append(matrix[row][col])
				col=col+1
				dir=4
		return spiral_list
s=Solution()
print s.spiralOrder([
 [1],[2],[3]
])