import os
class Solution(object):
	def multiply(self, num1, num2):
		if len(num1)<len(num2):
			tmp=num2
			num2=num1
			num1=tmp
		media_results=[]
		mult_numbers=[]
		for i in range(len(num1)-1,-1,-1):
			mult_numbers.append(int(num1[i]))
		
		max_digit=0
		for i in range(len(num2)-1,-1,-1):
			base_n=int(num2[i])
			numbers=[0]*(len(num2)-1-i)
			carry=0
			for j in range(len(mult_numbers)):
				n=mult_numbers[j]*base_n+carry
				numbers.append(n%10)
				carry=n/10
			if carry!=0:
				numbers.append(carry)
			if max_digit<len(numbers):
				max_digit=len(numbers)
			media_results.append(numbers)
		result=[]
		carry=0
		for i in range(max_digit):
			n=0
			for j in range(len(media_results)):
				if i>=len(media_results[j]):
					continue
				n=n+media_results[j][i]
			n=n+carry
			result.append(n%10)
			carry=n/10
		if carry>0:
			result.append(carry)
		result.reverse()
		result_str=''
		ind=0
		for i in range(len(result)):
			if i==ind and result[i]==0 and ind!=len(result)-1:
				ind=ind+1
				continue
			result_str=result_str+str(result[i])
		return result_str
s=Solution()
print s.multiply('123','456')
			