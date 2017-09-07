class Solution:
	def subsetsWithDup(self, S):
		# write your code here
		S.sort()
		p = [[S[x] for x in range(len(S)) if i>>x&1] for i in range(2**len(S))]
		func = lambda x,y:x if y in x else x + [y]
		p = reduce(func, [[], ] + p)
		return list(reversed(p))
		
	def DFS(self,S,cur_id,results):
		if cur_id==len(S):
			return
		if cur_id!=len(S)-1 and S[cur_id]==S[cur_id+1]:
			begin_id=cur_id
			while S[cur_id]==S[begin_id] and cur_id!=len(S)-1:
				cur_id=cur_id+1
			if S[cur_id]!=S[begin_id]:
				cur_id=cur_id-1
			end_id=cur_id
			l=len(results)
			for k in range(l):
				for i in range(begin_id,end_id+1):
					new_res=results[k][:]
					for j in range(begin_id,i+1):
						new_res.append(S[begin_id])
					results.append(new_res)
		else:
			l=len(results)
			for i in range(l):
				new_res=results[i][:]
				new_res.append(S[cur_id])
				results.append(new_res)
		self.DFS(S,cur_id+1,results)
			
	def subsetsWithDup2(self, S):
		if len(S)==0:
			return []
		if len(S)==1:
			return [[],S]
		results=[[]]
		S.sort()
		self.DFS(S,0,results)
		return results
		
s=Solution()
print s.subsetsWithDup2([1,1,2,2])
		