import os
class Solution(object):
	def DFS(self,cur_id,cur_dep,n,k,cur_res,results):
		if cur_dep==k:
			results.append(cur_res[:])
		else:
			for i in range(cur_id,n):
				cur_res.append(i+1)
				self.DFS(i+1,cur_dep+1,n,k,cur_res,results)
				cur_res.pop()
					
	def combine(self, n, k):
		if k==1:
			return [[i] for i in range(1,n+1)]
		results=[]
		self.DFS(0,0,n,k,[],results)
		return results
		
s=Solution()
print s.combine(4,2)