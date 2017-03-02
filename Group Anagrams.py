class Solution(object):
	def groupAnagrams(self, strs):
		results=[]
		map={}
		for i in range(len(strs)):
			chars=strs[i]
			origin_str=chars
			chars = "".join((lambda x:(x.sort(),x)[1])(list(chars)))
			if chars in map:
				ind=map[chars]
				results[ind].append(origin_str)
			else:
				map[chars]=len(results)
				results.append([origin_str])
		return results
s=Solution()
print s.groupAnagrams(["and","dan"])
			