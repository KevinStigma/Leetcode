class Solution(object):
	def longestValidParentheses(self, s):
		stack=[]
		max_length=0
		for i in range(len(s)):
			if s[i]=='(':
				stack.append(i)
			else:
				if len(stack)==0 or s[stack[-1]]==')':
					stack.append(i)
				else:
					stack.pop()
					length=0
					if len(stack)==0:
						length=i+1
					else:
						length=i-stack[-1]
					max_length=max(max_length,length)
		return max_length
s=Solution()
print s.longestValidParentheses("()()")
			
			
		
		