class Solution(object):
	def isScramble(self, s1, s2):
		if len(s1)!=len(s2):
			return False
		if len(s1)==0:
			return True
		if s1==s2:
			return True
		ss1="".join((lambda x:(x.sort(),x)[1])(list(s1)))
		ss2="".join((lambda x:(x.sort(),x)[1])(list(s2)))
		if ss1!=ss2:
			return False
		l=len(s1)
		for i in range(1,l):
			if self.isScramble(s1[0:i],s2[0:i]) and self.isScramble(s1[i:],s2[i:]):
				return True
			if self.isScramble(s1[0:i],s2[l-i:]) and self.isScramble(s1[i:],s2[0:l-i]):
				return True
		return False