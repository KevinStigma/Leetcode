class Solution(object):
	def trap(self, height):
		if len(height)==0 or len(height)==1:
			return 0
		right_max=[0]*len(height)
		left_max=[0]*len(height)
		left_max[0]=height[0]
		for i in range(1,len(height)):
			left_max[i]=max(left_max[i-1],height[i])
		right_max[-1]=height[-1]
		for i in range(len(height)-2,-1,-1):
			right_max[i]=max(right_max[i+1],height[i])
		waters=0
		for i in range(len(height)):
			if i!=1 or i!=len(height)-1:
				if right_max[i]>height[i] and left_max[i]>height[i]:
					waters=waters+(min(right_max[i],left_max[i])-height[i])
		return waters
			
s=Solution()
print s.trap([2,0,2])
				
				
			
			
			
			
			
			
		
		
		