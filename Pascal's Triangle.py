class Solution(object):
	def generate(self, numRows):
		pascal_triangle=[]	
		for i in range(numRows):
			cur_list=[1]
			if i>=1:
				pre_list=pascal_triangle[i-1]
				for j in range(i-1):
					cur_list.append(pre_list[j]+pre_list[j+1])
				cur_list.append(1)
			pascal_triangle.append(cur_list)	
		return pascal_triangle
s=Solution()
print s.generate(2)