class Solution(object):
	def largestRectangleArea(self, heights):
		if len(heights)==0:
			return 0
		index=0
		heights.append(-1)
		stack=[]
		max_area=-1
		while index<len(heights):
			if len(stack)==0 or heights[stack[-1]]<=heights[index]:
				stack.append(index)
				index=index+1
			else:
				pop=stack.pop()
				if len(stack)==0:
					max_area=max(max_area,heights[pop]*index)
				else:
					max_area=max(max_area,heights[pop]*(index-stack[-1]-1))
		return max_area
s=Solution()
print s.largestRectangleArea([4,2,0,3,2,5])