class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		queue=[(beginWord,1)]
		if not (endWord in wordList):
			return 0
		visited={}
		for word in wordList:
			visited[word]=False
		
		while len(queue)!=0:
			res=queue.pop(0)
			cur_word=res[0]
			cur_len=res[1]
			if cur_word==endWord:
				return cur_len
			for i in range(len(beginWord)):
				left_word=cur_word[:i]
				right_word=cur_word[i+1:]
				for letter in 'abcdefghijklmnopqrstuvwxyz':
					if letter==cur_word[i]:
						continue
					new_word=left_word+letter+right_word
					if new_word in visited:
						if visited[new_word]==True:
							continue
						queue.append((new_word,res[1]+1))
						visited[new_word]=True
		return 0
s=Solution()
print s.ladderLength("hit","cog",["hot","dot","dog","lot","log"])
		
		
		