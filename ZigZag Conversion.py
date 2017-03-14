class Solution(object):
	def convert(self, s, numRows):
		if len(s)==1 or numRows==1:
			return s
		length=len(s)
		string_rows=['' for i in range(numRows)]
		i=0
		count=0
		while i<length:
			if count==0:
				line=''
				if length-i>=numRows:
					line=s[i:i+numRows]
				else:
					line=s[i:]
				for j in range(len(line)):
					string_rows[j]+=line[j]
				i=i+numRows
			else:
				string_rows[numRows-count-1]+=s[i]
				i=i+1
			count=(count+1)%(numRows-1)
		result=''
		for i in range(numRows):
			result+=string_rows[i]
		return result
s=Solution()
print s.convert('AB',3)
				
			