class Solution(object):
	def __init__(self):
		self.queen=[]
		self.result=[]
		self.n=0
	def valid(self,row,col):
		queen=self.queen
		for i in range(row):
			if queen[i]==col:
				return False
			if abs(queen[i]-col)==abs(row-i):
				return False
		return True
		
	def DFS(self,row):
		if row==self.n:
			solution=[]
			for i in range(self.n):
				tmp_str=""
				for j in range(self.n):
					if j!=self.queen[i]:
						tmp_str=tmp_str+'.'
					else:
						tmp_str=tmp_str+'Q'
				solution.append(tmp_str)
			self.result.append(solution)
			return True
		pass_count=0
		for i in range(self.n):
			self.queen[row]=i
			if self.valid(row,i) and self.DFS(row+1):
				pass_count=pass_count+1
		if pass_count==0:
			return False
		return True
		
	def solveNQueens(self, n):
		self.queen=[-1]*n
		self.result=[]
		self.n=n
		self.DFS(0)
		return self.result
		
s=Solution()
print s.solveNQueens(1)