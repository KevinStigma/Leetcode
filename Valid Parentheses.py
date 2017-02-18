class Solution(object):
	def isValid(self, s):
		stack=[]
		map={')':'(','}':'{',']':'['}
		for char in s:
			if char=='(' or char=='{' or char=='[':
				stack.append(char)
			else:
				if len(stack)==0:
					return False
				top=stack.pop()
				if top!=map[char]:
					return False
		if len(stack)!=0:
			return False
		return True

			