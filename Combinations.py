import os
class Solution(object):
	def combine(self, n, k):
		if k == 1:
			return [[i + 1] for i in range(n)]
		result = []
		if n > k:
			result = [r + [n] for r in self.combine(n - 1, k - 1)]+ self.combine(n - 1, k)
		else:
			result = [r + [n] for r in self.combine(n - 1, k - 1)]
		return result
s=Solution()
print s.combine(4,2)