class Solution(object):
	def maxProfit(self, prices):
		i=0
		profit=0
		while i<len(prices)-1:
			for j in range(i+1,len(prices)):
				if prices[j]>prices[j-1]:
					break
			if j==len(prices)-1 and prices[j]<prices[j-1]:
				return profit
			ind=j-1
			for j in range(ind+1,len(prices)):
				if prices[j]<prices[j-1]:
					break
			if j==len(prices)-1 and prices[j]>=prices[j-1]:
				j=len(prices)
			profit=profit+(prices[j-1]-prices[ind])
			i=j
		return profit
s=Solution()
print s.maxProfit([2,1,2,0,1])
			
			