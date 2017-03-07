class Solution(object):
	def plusOne(self, digits):
		added_num=[]
		for i in range(len(digits)-1,-1,-1):
			if digits[i]!=9:
				added_num.append(digits[i]+1)
				for j in range(i-1,-1,-1):
					added_num.append(digits[j])
				break
			else:
				added_num.append(0)
		if i==0 and digits[i]==9:
			added_num.append(1)
		added_num.reverse()
		return added_num
s=Solution()
print s.plusOne([9,9,9,9])
				