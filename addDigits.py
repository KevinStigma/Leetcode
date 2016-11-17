def sumDigits(num):
	sum=0
	while num!=0:
		sum=sum+num%10
		num=int(num/10)
	return sum
		
class Solution(object):
	def addDigits(self, num):
		sum=sumDigits(num)
		while sum>=10:
			sum=sumDigits(sum)
		return sum
		
sol=Solution()
sol.addDigits(38)
        