class Solution(object):
	def initVisited(self,visited):
		for word in visited:
			visited[word]=0
	def allVisited(self,visited,word_map):
		if len(word_map)!=len(visited):
			return False
		for word in visited:
			if visited[word]!=word_map[word]:
				return False
		return True
	def findSubstring(self, s, words):
		if len(s)==0 or len(words)==0:
			return []
		sl=len(s)
		l=len(words[0])
		inds=[]
		word_map={}
		for word in words:
			if not (word in word_map):
				word_map[word]=1
			else:
				word_map[word]=word_map[word]+1
		visited={}
		for word in words:
			visited[word]=0
		for i in range(l):
			low=i
			high=i
			self.initVisited(visited)
			while high<sl:
				if high+l>sl:
					break
				cur_str=s[high:high+l]
				if not(cur_str in word_map):
					low=high+l
					high=low
					self.initVisited(visited)
					continue
				if visited[cur_str]<word_map[cur_str]:
					visited[cur_str]=visited[cur_str]+1
				else:
					while s[low:low+l]!=cur_str:
						visited[s[low:low+l]]=visited[s[low:low+l]]-1
						low=low+l
					low=low+l
				if self.allVisited(visited,word_map):
					inds.append(high-l*(len(words)-1))
				high=high+l
		return inds
s=Solution()
print s.findSubstring("barfoothefoobarman",["foo", "bar"])