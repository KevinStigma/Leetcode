class Solution(object):
	#O(n^2)'s solution
	def canCompleteCircuit1(self, gas, cost):
		if len(gas)==0:
			return -1
		surplus=[0 for i in range(len(gas))]
		for i in range(len(gas)):
			surplus[i]=gas[i]-cost[i]
		for i in range(len(surplus)):
			j=i
			cur_gas=surplus[j]
			if cur_gas<0:
				continue
			j=(j+1)%len(surplus)
			while j!=i:
				cur_gas=cur_gas+surplus[j]
				if cur_gas<0:
					break
				j=(j+1)%len(surplus)
			if j==i:
				return i
		return -1
	def canCompleteCircuit2(self, gas, cost):
		if len(gas)==0:
			return -1
		surplus=[0 for i in range(len(gas))]
		for i in range(len(gas)):
			surplus[i]=gas[i]-cost[i]
		start_id=0
		while start_id<len(surplus):
			j=start_id
			cur_gas=surplus[j]
			if cur_gas<0:
				start_id=start_id+1
				continue
			j=(j+1)%len(surplus)
			while j!=start_id:
				cur_gas=cur_gas+surplus[j]
				if cur_gas<0:
					break
				j=(j+1)%len(surplus)
			if j==start_id:
				return start_id
			else:
				if j<start_id:
					return -1
				start_id=j+1
		return -1
	#O(n)'s solution	
	def canCompleteCircuit3(self, gas, cost):
		if len(gas)==0:
			return -1
		surplus=[0 for i in range(len(gas))]
		for i in range(len(gas)):
			surplus[i]=gas[i]-cost[i]
		i=0
		start_id=0
		sum=0
		total=0
		for i in range(len(surplus)):
			sum=sum+surplus[i]
			total=total+surplus[i]
			if sum<0:
				sum=0
				start_id=i+1
		if total<0:
			return -1
		else:
			return start_id