class Solution(object):
	def __init__(self):
		self.queen=[]
		self.result_num=0
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
			#solution=[]
			for i in range(self.n):
				tmp_str=""
				for j in range(self.n):
					if j!=self.queen[i]:
						tmp_str=tmp_str+'.'
					else:
						tmp_str=tmp_str+'Q'
				print tmp_str
				#solution.append(tmp_str)
			
			self.result_num=self.result_num+1
			return True
		pass_count=0
		for i in range(self.n):
			self.queen[row]=i
			if self.valid(row,i) and self.DFS(row+1):
				pass_count=pass_count+1
		if pass_count==0:
			return False
		return True
		
	def totalNQueens(self, n):
		self.queen=[-1]*n
		self.result_num=0
		self.n=n
		self.DFS(0)
		return self.result_num
		
s=Solution()
print s.totalNQueens(1)