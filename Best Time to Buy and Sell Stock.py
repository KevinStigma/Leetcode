class Solution(object):
	def maxProfit(self, prices):
		if len(prices)==0 or len(prices)==1:
			return 0
		min_value=prices[0]
		max_profit=0
		for i in range(1,len(prices)):
			if min_value<prices[i]:
				max_profit=max(max_profit,prices[i]-min_value)
			else:
				min_value=prices[i]
		return max_profit
s=Solution()
print s.maxProfit([7, 1, 5, 3, 6, 4])
		