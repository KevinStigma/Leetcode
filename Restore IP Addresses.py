class Solution(object):
	def __init__(self):
		self.results=[]
	def validNum(self,num):
		if num>=0 and num<=255:
			return True
		return False
	def processResults(self):
		reses=[]
		for res in self.results:
			s=""
			for i in range(4):
				s=s+str(res[i])
				if i!=3:
					s=s+"."
			reses.append(s)
		return reses
		
	def backTracing(self,s,cur_id,result,depth):
		if depth>4:
			if cur_id!=len(s):
				return
			self.results.append(result[:])
			return
		if cur_id>=len(s):
			return
		for i in range(1,4):
			if cur_id+i>len(s):
				continue
			if s[cur_id]=='0' and i>1:
				continue
			num=int(s[cur_id:cur_id+i])
			if self.validNum(num)==False:
				continue
			result.append(num)
			self.backTracing(s,cur_id+i,result,depth+1)
			result.pop()
		
	def restoreIpAddresses(self, s):
		self.results=[]
		self.backTracing(s,0,[],1)
		return self.processResults()
s=Solution()
print s.restoreIpAddresses("010010")