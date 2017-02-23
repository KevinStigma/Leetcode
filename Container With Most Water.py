class Solution(object):
	def maxArea(self, height):
		max_area=0
		cur_h=min(height[0],height[-1])
		h=cur_h
		w=len(height)-1
		max_area=h*w
		i=0
		j=len(height)-1
		while i<j:
			while i<j and height[i]<=cur_h:
				i=i+1
			while i<j and height[j]<=cur_h:
				j=j-1
			cur_h=min(height[j],height[i])
			max_area=max(max_area,(j-i)*cur_h)
		return max_area
s=Solution()
s.maxArea([2,1])