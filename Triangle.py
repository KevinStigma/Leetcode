class Solution(object):
	def minimumTotal(self, triangle):
		sum=0
		if len(triangle)==0:
			return 0
		path_sum=[]
		for i in range(len(triangle)):
			path_sum.append([0 for i in range(len(triangle[i]))])
		path_sum[0][0]=triangle[0][0]
		for i in range(1,len(triangle)):
			for j in range(len(triangle[i])):
				if j==0:
					path_sum[i][j]=path_sum[i-1][0]+triangle[i][j]
				elif j==len(triangle[i])-1:
					path_sum[i][j]=path_sum[i-1][-1]+triangle[i][j]
				else:
					path_sum[i][j]=min(path_sum[i-1][j],path_sum[i-1][j-1])+triangle[i][j]
		sum=path_sum[-1][0]
		for i in range(1,len(path_sum[-1])):
			sum=min(sum,path_sum[-1][i])
		return sum
s=Solution()
print s.minimumTotal([[-1],[2,3],[1,-1,-3]])
				
			
			
		
		
		