class Solution(object):
	def longestValidParentheses(self, s):
		stack1=[]
		stack2=[]
		max_length=0
		for i in range(len(s)):
			cur_char=s[i]
			if len(stack1)==0:
				stack1.append(cur_char)
				stack2.append(i)
			else:
				if cur_char==')' and stack1[-1]=='(':
					stack1.pop()
					stack2.pop()
					if len(stack2)==0:
						max_length=max(max_length,i+1)
					else:
						max_length=max(max_length,i-stack2[-1])
				else:
					stack1.append(cur_char)
					stack2.append(i)
		return max_length
s=Solution()
print s.longestValidParentheses("()()")
			
			
		
		