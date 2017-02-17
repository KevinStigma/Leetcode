permutations=[]
visited=[]
one_permu=[]
def DFS(nums,start_id):
	global visited
	global one_permu
	global permutations
	if len(one_permu)==len(nums):
		item=[]
		for num in one_permu:
			item.append(num)
		permutations.append(item)
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
		global visited
		global one_permu
		global permutations
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
print s.permute([1])