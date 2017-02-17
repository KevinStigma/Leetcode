permutations=[]
visited=[]
one_permu=[]
def DFS(nums):
	global visited,one_permu,permutations
	if len(one_permu)==len(nums):
		#we can't use 'permutations.append(one_permu), because the value of one_permu will change later, so 
		#we must append a list of deep copy of one_permu
		permutations.append(list(one_permu))
		return
	for i in range(len(nums)):
		if visited[i]==True:
			continue
		visited[i]=True
		one_permu.append(nums[i])
		DFS(nums)
		visited[i]=False
		one_permu.pop()

class Solution(object):
	def permute(self, nums):
		global visited,one_permu,permutations
		one_permu=[]
		permutations=[]
		visited=[False for j in range(len(nums))]
		DFS(nums)
		return permutations
s=Solution()
print s.permute([1,2,3])