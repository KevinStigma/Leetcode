class Solution(object):
	def romanToInt(self, s):
		charsSet=['I','V','X','L','C','D','M']
		corInteger=[1,5,10,50,100,500,1000]
		l=len(s)
		num=0
		for i in range(l-1,-1,-1):
			char=s[i]
			ind=charsSet.index(char)
			if i!=l-1:
				preChar=s[i+1]
				preInd=charsSet.index(preChar)
				if ind<preInd:
					num=num-corInteger[ind]
				else:
					num=num+corInteger[ind]
			else:
				num=num+corInteger[ind]
		return num
		
s=Solution()
s.romanToInt('DCXXI')
			
	