#this code is too hacky. For more detail, we can view the following article:http://www.cnblogs.com/youngforever/archive/2013/07/08/3178379.html 
class Solution(object):
	def myAtoi(self, str):
		max_int=2147483647
		min_int=-2147483648
		if str=="":
			return 0
		start_ind=-1
		end_ind=-1
		for i in range(len(str)):
			if str[i]!=' ':
				if str[i].isdigit() or ((i!=len(str)-1) and (str[i]=='-' or str[i]=='+') and str[i+1].isdigit()):
					start_ind=i
				break
		if start_ind==-1:
			return 0
		for j in range(start_ind+1,len(str)):
			if not str[j].isdigit():
				end_ind=j
				break
		if end_ind==-1:
			end_ind=len(str)
		num_str=str[start_ind:end_ind]
		if num_str[0]=='-':
			num = int(num_str[1:])*(-1)
			if num<min_int:
				num=min_int
			return num
		elif num_str[0]=='+':
			num=int(num_str[1:])
			if num>max_int:
				num=max_int
			return num
		else:
			num=int(num_str)
			if num>max_int:
				num=max_int
			return num
			
s=Solution()
print s.myAtoi("-2147483649")
		