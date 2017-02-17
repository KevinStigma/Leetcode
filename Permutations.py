permutations=[]
visited=[]
one_permu=[]
def DFS(nums,start_id):
	global visited,one_permu,permutations
	if len(one_permu)==len(nums):
		#we can't use 'permutations.append(one_permu), because the value of one_permu will change later, so 
		#we must append a list of deep copy of one_permu
		permutations.append(list(one_permu))
		return
	for i in range(len(nums)):
		if i==start_id:
			continue
		if visited[i]==True:
			continue
		visited[i]=True
		one_permu.append(nums[i])
		DFS(nums,i)
		visited[i]=False
		one_permu.pop()

class Solution(object):
	def permute(self, nums):
		global visited,one_permu,permutations
		one_permu=[]
		permutations=[]
		visited=[False for j in range(len(nums))]
		for i in range(len(nums)):
			for j in range(len(visited)):
				visited[j]=False
			one_permu=[nums[i]]
			visited[i]=True
			DFS(nums,i)
			visited[i]=False
			one_permu.pop()
		return permutations
s=Solution()
print s.permute([1,2,3])