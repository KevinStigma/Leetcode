# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def insert(self, intervals, newInterval):
		new_intervals=[]
		if len(intervals)==0:
			return [newInterval]
		ind=-2
		for i in range(len(intervals)):
			interval=Interval(intervals[i].start,intervals[i].end)
			if interval.end<newInterval.start:
				new_intervals.append(interval)
			else:
				if newInterval.end<interval.start:
					new_intervals.append(newInterval)
					ind=i-1
				else:
					interval.end=max(interval.end,newInterval.end)
					interval.start=min(interval.start,newInterval.start)
					new_intervals.append(interval)
					ind=i
				break
		if ind==-2:
			new_intervals.append(newInterval)
		else:
			for i in range(ind+1,len(intervals)):	
				interval=intervals[i]
				end_interval=new_intervals[-1]
				if interval.start<=end_interval.end:
					new_intervals[-1].end=max(interval.end,end_interval.end)
				else:
					new_intervals.append(interval)
		return new_intervals
		