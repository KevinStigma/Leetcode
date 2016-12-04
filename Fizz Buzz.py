class Solution(object):
	def fizzBuzz(self, n):
		str_list=[]
		for i in range(n):
			num=i+1
			if num%3==0 and num%5==0:
				str_list.append('FizzBuzz')
			elif num%3==0:
				str_list.append('Fizz')
			elif num%5==0:
				str_list.append('Buzz')
			else:
				str_list.append(str(num))
		return str_list
		
s=Solution()
print s.fizzBuzz(15)