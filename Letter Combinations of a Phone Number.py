class Solution(object):
	def __init__(self):
		self.contain_letters=[' ','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
		
	def letterCombinations(self, digits):
		if len(digits)==0:
			return []
		if len(digits)==1:
			letters=self.contain_letters[int(digits[0])]
			return [letter for letter in letters]
		num=int(digits[0])
		combinations=[]
		contains=self.contain_letters[num]
		for c in contains:
			exist_combins=self.letterCombinations(digits[1:])
			for s in exist_combins:
				combinations.append(c+s)
		return combinations
s=Solution()
print s.letterCombinations('23')