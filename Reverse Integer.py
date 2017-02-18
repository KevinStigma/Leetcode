class Solution(object):
	def computePositiveReverse(self,num):
		num_list=[]
		while num!=0:
			num_list.append(num%10)
			num=int(num/10)
		reve_num=0
		base=1
		for n in num_list[::-1]:
			reve_num=reve_num+base*n
			base=base*10
		return reve_num
		
	def reverse(self, x):
		maxInt=2147483647
		minInt=-2147483648
		if x==0:
			return 0
		elif x>0:
			num=self.computePositiveReverse(x)
			if num>maxInt:
				return 0
			else:
				return num
		else:
			num=-self.computePositiveReverse(-x)
			if num<minInt:
				return 0
			else:
				return num
s=Solution()
print s.reverse(-12)