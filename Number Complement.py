class Solution(object):
	def findComplement(self, num):
		new_num=0
		base=1
		while num!=0:
			bit=num%2
			if bit==0:
				new_num=new_num+base
			num=num/2
			base=base*2
		return new_num
s=Solution()
print s.findComplement(10)