import os
class Solution(object):
	def __init__(self):
		self.visited=[]
	def DFS(self,board,word,cur_ind,row,col):
		if cur_ind==len(word)-1:
			return True
		self.visited[row][col]=True
		if row>0 and board[row-1][col]==word[cur_ind+1] and self.visited[row-1][col]==False:
			if self.DFS(board,word,cur_ind+1,row-1,col):
				return True
		
		if row<len(board)-1 and board[row+1][col]==word[cur_ind+1] and self.visited[row+1][col]==False:
			if self.DFS(board,word,cur_ind+1,row+1,col):
				return True
		
		if col>0 and board[row][col-1]==word[cur_ind+1] and self.visited[row][col-1]==False:
			if self.DFS(board,word,cur_ind+1,row,col-1):
				return True
			
		if col<len(board[0])-1 and board[row][col+1]==word[cur_ind+1] and self.visited[row][col+1]==False:
			if self.DFS(board,word,cur_ind+1,row,col+1):
				return True
		self.visited[row][col]=False #don't forget!
		return False

	def exist(self, board, word):
		if board==[]:
			return False
		m=len(board)
		n=len(board[0])
		for i in range(m):
			for j in range(n):
				if board[i][j]==word[0]:
					self.visited=[[False]*n for k in range(m)]
					if self.DFS(board,word,0,i,j):
						return True
		return False
s=Solution()
print s.exist(["ABCE","SFES","ADEE"],"ABCESEEEFS")