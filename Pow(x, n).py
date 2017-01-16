class Solution(object):
	def PositivePow(self,x,n):
		sum=x
		exponent=1
		mult_num=x
		add_exp=1
		while exponent!=n:
			if(exponent+add_exp*2>n):
				add_exp=1
				mult_num=x
				exponent=exponent+add_exp
				sum=sum*mult_num
				continue
			add_exp=add_exp*2
			exponent=exponent+add_exp
			mult_num=mult_num*mult_num
			sum=sum*mult_num
		return sum
	def myPow(self, x, n):
		if n==0:
			return 1
		elif n>0:
			return self.PositivePow(x,n)
		else:
			return 1/self.PositivePow(x,-n)
			

s=Solution()
print s.myPow(34.00515,-3)
