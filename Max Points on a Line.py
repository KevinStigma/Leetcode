# Definition for a point.
class Point(object):
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

class Solution(object):
	def maxPoints(self, points):
		if(len(points)==0):
			return 0
		if(len(points)==1):
			return 1
		max_num=0
		for j in range(0,len(points)):
			map={}
			pt=points[j]
			special_slop_num=1 #x coordinate
			equal_num=0
			for i in range(0,len(points)):
				if i==j:
					continue
				if pt.y==points[i].y:
					if pt.x==points[i].x:
						equal_num=equal_num+1
					else:
						special_slop_num=special_slop_num+1
				else:
					slope=(float)(points[i].x-pt.x)/(float)(points[i].y-pt.y)
					if not (slope in map):
						map[slope]=2
					else:
						map[slope]=map[slope]+1
			max_num=max(special_slop_num+equal_num,max_num)
			for slope_set in map:
				max_num=max(max_num,map[slope_set]+equal_num)
		return max_num
s=Solution()
print s.maxPoints([Point(-4,-4),Point(-8,-582),Point(-3,-3),Point(-9,-651),Point(9,591)])