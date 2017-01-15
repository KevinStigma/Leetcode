class Solution(object):
	def getRow(self, rowIndex):
		row_list=[0 for i in range(rowIndex+1)]
		row_list[0]=1
		for i in range(rowIndex):
			for j in range(i+1,0,-1):
				row_list[j]=row_list[j]+row_list[j-1]
		return row_list
s=Solution()
print s.getRow(0)