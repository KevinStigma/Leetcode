class Solution(object):
	def divide(self, dividend, divisor):
		max_int=(1<<31)-1
		a=abs(dividend)
		b=abs(divisor)
		if b==0:
			return max_int
		if dividend==0:
			return 0
		res=0
		while a>=b:
			tmp=b
			s=1
			while (tmp<<1)<=a:
				tmp=tmp<<1
				s=s*2
			res=res+s
			a=a-tmp
		minus=False
		if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
			minus=True
		if res>max_int and minus==False:
			return max_int
		elif res>max_int+1 and minus==True:
			return max_int
		if minus:
			return -res
		return res

s=Solution()
print s.divide(-2147483648,1)
					
		
		
		