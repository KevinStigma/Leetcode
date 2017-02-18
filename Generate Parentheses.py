class Solution(object):
	def __init__(self):
		self.combinations=[]
		self.max_bracket=0
		
	def DFS(self,cur_str,exist_bracket,closed_bracket):
		if closed_bracket==self.max_bracket:
			self.combinations.append(cur_str)
			return
		if exist_bracket<self.max_bracket:
			exist_bracket=exist_bracket+1
			self.DFS(cur_str+"(",exist_bracket,closed_bracket)
			exist_bracket=exist_bracket-1
		if closed_bracket<exist_bracket:
			closed_bracket=closed_bracket+1
			self.DFS(cur_str+")",exist_bracket,closed_bracket)
			closed_bracket=closed_bracket-1
		
	def generateParenthesis(self, n):
		exist_bracket=0
		closed_bracket=0
		self.combinations=[]
		self.max_bracket=n
		self.DFS("",exist_bracket,closed_bracket)
		return self.combinations
s=Solution()
print s.generateParenthesis(0)
		