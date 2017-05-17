# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start=s
		self.end=e

class Solution(object):
	def merge(self, intervals):
		if len(intervals)==0 or len(intervals)==1:
			return intervals
		intervals.sort(lambda x,y:cmp(x.start,y.start))
		new_intervals=[]
		new_intervals.append(intervals[0])
		for i in range(1,len(intervals)):
			interval=intervals[i]
			pre=new_intervals[-1]
			if interval.start<=pre.end:
				new_intervals[-1].end=max(new_intervals[-1].end,interval.end)
			else:
				new_intervals.append(interval)
		return new_intervals
		
intervals=[Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)]
s=Solution()
new_intervals=s.merge(intervals)
for interval in new_intervals:
	print interval.start
	print interval.end