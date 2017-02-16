class Solution(object):
	def candy(self, ratings):
		candy=[1 for i in range(len(ratings))]
		for i in range(1,len(candy)):
			if ratings[i]>ratings[i-1]:
				candy[i]=candy[i-1]+1
		
		for i in range(len(candy)-1,0,-1):
			if ratings[i-1]>ratings[i]:
				candy[i-1]=max(candy[i-1],candy[i]+1)
		sum=0
		for num in candy:
			sum=sum+num
		return sum
		
s=Solution()
print s.candy([1,2,2])