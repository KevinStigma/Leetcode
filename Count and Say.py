class Solution(object):
	def countAndSay(self, n):
		cur_num='1'
		new_num=''
		for i in range(n-1):
			new_num=''
			count=1
			for j in range(1,len(cur_num)):
				if cur_num[j]==cur_num[j-1]:
					count=count+1
				else:
					value=cur_num[j-1]
					new_num=new_num+str(count)+value
					count=1
			new_num=new_num+str(count)+cur_num[-1]
			cur_num=new_num
		return cur_num
s=Solution()
print s.countAndSay(8)