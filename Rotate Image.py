class Solution(object):
	#we should record some O(1) space complexity solution
	def rotate(self, matrix):
		n=len(matrix)
		rot_matrix=[[0]*n for i in range(n)]
		for i in range(n):
			for j in range(n):
				rot_matrix[j][n-i-1]=matrix[i][j]
		for i in range(n):
			for j in range(n):
				matrix[i][j]=rot_matrix[i][j]
s=Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])