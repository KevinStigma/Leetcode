class Solution(object):
	def __init__(self):
		self.__lookupTable=[0 for i in range(0,1000)]
		self.__lookupTable[1]=1
		self.__lookupTable[2]=1
		self.__lookupTable[3]=1
		self.__lookupTable[4]=-1
	#It is my initial version of brute force, true but time exceed
	def statusSearch(self,result_num,level):
		if (result_num>=1 and result_num<=3):
			if level%2==1:
				return True
			else:
				return False
		if not self.__lookupTable[result_num]==0 and level%2==1:
			return self.__lookupTable[result_num]>0
		
		if level%2==1:
			for i in range(1,4):
				isWin=self.statusSearch(result_num-i,level+1)
				if isWin==True:
					self.__lookupTable[result_num]=1
					return True
			self.__lookupTable[result_num]=-1
			return False
		else:
			for i in range(1,4):
				isWin=self.statusSearch(result_num-i,level+1)
				if isWin==False:
					self.__lookupTable[result_num]=-1
					return False
			self.__lookupTable[result_num]=1
			return True

	def canWinNim(self, n):
		#return self.statusSearch(n,1)
		return n%4!=0
s=Solution()
print s.canWinNim(5)