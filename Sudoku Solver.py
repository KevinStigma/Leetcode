import os
class Solution(object):
	def DFS(self,row,col,row_visited,col_visited,pala_visited,num_board):
		for i in range(row,9):
			for j in range(col,9):
				if num_board[i][j]==0:
					for n in range(9):
						if row_visited[i][n]==True:
							continue
						if col_visited[j][n]==True:
							continue
						ind=int(i/3)*3+int(j/3)
						if pala_visited[ind][n]==True:
							continue
						row_visited[i][n]=True
						col_visited[j][n]=True
						pala_visited[ind][n]=True
						num_board[i][j]=n+1
						begin_row=row
						begin_col=col
						if col==8:
							begin_row=begin_row+1
							begin_col=0
						if self.DFS(begin_row,begin_col,row_visited,col_visited,pala_visited,num_board):
							return True
						row_visited[i][n]=False
						col_visited[j][n]=False
						pala_visited[ind][n]=False
						num_board[i][j]=0
					return False
		return True
		
		
	def solveSudoku(self, board):
		num_board=[[0]*9 for i in range(9)]
		for i in range(9):
			for j in range(9):
				if board[i][j]!='.':
					num_board[i][j]=int(board[i][j])
		
		row_visited=[[False]*9 for i in range(9)]
		col_visited=[[False]*9 for i in range(9)]
		pala_visited=[[False]*9 for i in range(9)]
		for i in range(9):
			for j in range(9):
				if num_board[i][j]!=0:
					row_visited[i][num_board[i][j]-1]=True
		
		for i in range(9):
			for j in range(9):
				if num_board[j][i]!=0:
					col_visited[i][num_board[j][i]-1]=True
		
		for i in range(3):
			for j in range(3):
				ind=i*3+j
				begin_row=i*3
				begin_col=j*3
				end_row=begin_row+2
				end_col=begin_col+2
				for r in range(begin_row,end_row+1):
					for c in range(begin_col,end_col+1):
						if num_board[r][c]!=0:
							pala_visited[ind][num_board[r][c]-1]=True
							
		self.DFS(0,0,row_visited,col_visited,pala_visited,num_board)
		print num_board
		
s=Solution()
s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])