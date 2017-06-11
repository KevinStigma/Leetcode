class Solution(object):	
	def genGrayCode(self,n):
		if n==1:
			return [0,1]
		list1=self.genGrayCode(n-1)
		list2=list1[::-1]
		for i in range(len(list2)):
			list2[i]=list2[i]+(1<<(n-1))
		result=[]
		for num in list1:
			result.append(num)
		for num in list2:
			result.append(num)
		return result
		
	def grayCode(self, n):
		if n==0:
			return [0]
		return self.genGrayCode(n)
		
s=Solution()
print s.genGrayCode(2)
		