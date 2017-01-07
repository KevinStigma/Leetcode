class Solution(object):
	def searchMatrix(self, matrix, target):
		m=len(matrix)
		if m==0:
			return False
		n=len(matrix[0])
		if n==0:
			return False
		for i in range(m):
			if target>=matrix[i][0] and target<=matrix[i][n-1]:
				count=matrix[i].count(target)
				if count>0:
					return True
		return False

s=Solution()
print s.searchMatrix([[]],3)