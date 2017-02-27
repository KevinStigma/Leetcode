class Solution(object):	
	def isValidSudoku(self, board):
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
					if row_visited[i][num_board[i][j]-1]==False:
						row_visited[i][num_board[i][j]-1]=True
					else:
						return False
		
		for i in range(9):
			for j in range(9):
				if num_board[j][i]!=0:
					if col_visited[i][num_board[j][i]-1]==False:
						col_visited[i][num_board[j][i]-1]=True
					else:
						return False
		
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
							if pala_visited[ind][num_board[r][c]-1]==False:
								pala_visited[ind][num_board[r][c]-1]=True
							else:
								return False
		return True
s=Solution()
print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])