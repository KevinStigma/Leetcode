class Solution(object):
	def findWords(self, words):
		lines=[['Q','W','E','R','T','Y','U','I','O','P'],['A','S','D','F','G','H','J','K','L'],['Z','X','C','V','B','N','M']]
		results=[]
		for word in words:
			first_col=0
			first_row=0			
			for row in range(3):
				find=False
				for col in range(len(lines[row])):
					if lines[row][col]==word[0].upper():
						first_col=col
						first_row=row
						find=True
						break
				if find==True:
					break

			find=True
			for i in range(1,len(word)):
				if not word[i].upper() in lines[first_row]:
					find=False
					break
			if find:
				results.append(word)
		return results
s=Solution()
print s.findWords(["Hello", "Alaska", "Dad", "Peace"])