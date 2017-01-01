#in this question, we should pay attention to the occasion when the number is negative and the opeartor is division
class Solution(object):
	def __init__(self):
		self.stack_list=[]
	def operate(self,c):
		s=0
		if c=='+':
			s=self.stack_list[-1]+self.stack_list[-2]
		elif c=='-':
			s=self.stack_list[-2]-self.stack_list[-1]
		elif c=='*':
			s=self.stack_list[-2]*self.stack_list[-1]
		elif c=='/':
			s=int(self.stack_list[-2]/float(self.stack_list[-1]))
		self.stack_list.pop()
		self.stack_list[-1]=s
	def isDigit(self,s):
		if len(s)==1:
			if s.isdigit():
				return int(s)
			else:
				return None
		else:
			if s[0]=='-':
				return int(s[1:])*(-1)
			else:
				return int(s)
			
	def evalRPN(self,tokens):
		self.stack_list=[]
		for s in tokens:
			num=self.isDigit(s)
			if num!=None:
				self.stack_list.append(num)
			else:
				self.operate(s)
			print self.stack_list
			os.system('pause')
			
		return self.stack_list[0]
				
	
s=Solution()
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])