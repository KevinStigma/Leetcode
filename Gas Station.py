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
			
	#use dynamic programming
	def canCompleteCircuit4(self, gas, cost):
		gas_n=len(gas)
		diff=[0]*gas_n
		for i in range(gas_n):
			diff[i]=gas[i]-cost[i]
		sum=0
		for i in range(gas_n):
			sum=sum+diff[i]
		if sum<0:
			return -1
		p=[0]*gas_n
		p[0]=diff[0]
		max_value=p[0]
		max_ind=0
		for i in range(1,gas_n):
			if p[i-1]+diff[i]>=diff[i]:
				p[i]=p[i-1]+diff[i]
			else:
				p[i]=diff[i]
			if max_value<p[i]:
				max_ind=i
				max_value=p[i]
		max_list=[]
		for i in range(max_ind,-1,-1):
			if diff[i]<0:
				break
			max_list.append(i)
		max_list.reverse()	
		
		p[0]*gas_n
		p[0]=diff[0]
		min_value=p[0]
		min_ind=0
		for i in range(1,gas_n):
			if p[i-1]+diff[i]<=diff[i]:
				p[i]=p[i-1]+diff[i]
			else:
				p[i]=diff[i]
			if min_value>p[i]:
				min_ind=i
				min_value=p[i]
		min_list=[]
		for i in range(min_ind,-1,-1):
			if diff[i]>0:
				break
			min_list.append(i)
		min_list.reverse()
		if max_value>sum-min_value:
			return max_list[0]
		else:
			return (min_ind+1)%gas_n
		
		
s=Solution()
print s.canCompleteCircuit4([5],[4])
			