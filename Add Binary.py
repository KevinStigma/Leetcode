class Solution(object):
	def addBinary(self, a, b):
		max_digit=max(len(a),len(b))
		sum=""
		add=0
		for i in range(max_digit):
			num1=num2=0
			if i<len(a):
				num1=int(a[len(a)-i-1])
			if i<len(b):
				num2=int(b[len(b)-i-1])
			s=num1+num2+add
			add=s//2
			sum=sum+str(s%2)
		if add==1:
			sum=sum+"1"
		sum=sum[::-1]
		return sum

s=Solution()
print s.addBinary("10","111")