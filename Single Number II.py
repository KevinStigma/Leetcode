#we should use this problem to learn the konwledge about bit information
class Solution(object):
	def singleNumber(self, nums):
		mask_num=1
		res=0
		for i in range(32):
			sum=0
			bit=0
			for j in range(len(nums)):
				if nums[j]&mask_num!=0:
					sum=sum+1
			if sum%3!=0:
				bit=1
			else:
				bit=0
			if i==31 and bit==1:
				res=res-2147483647-1
				break
			res=res|(bit<<i)
			mask_num=mask_num*2
		return res

s=Solution()
print s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
