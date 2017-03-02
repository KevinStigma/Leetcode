class Solution(object):
	def fullJustify(self, words, maxWidth):
		used_word_count=0
		lines=[]
		while used_word_count<len(words):
			used_id=[used_word_count]
			length=len(words[used_word_count])
			used_word_count=used_word_count+1
			for i in range(used_word_count,len(words)):
				if length+len(words[i])+1<=maxWidth:
					used_id.append(i)
					used_word_count=used_word_count+1
					length=length+len(words[i])+1
				else:
					break
			line=''
			if len(used_id)==1 or used_word_count==len(words):
				for i in range(len(used_id)):
					line=line+words[used_id[i]]
					if i!=len(used_id)-1:
						line=line+' '
				length=len(line)
				for i in range(maxWidth-length):
					line=line+' '
			else:
				length=0
				print used_id
				for id in range(len(used_id)):
					length=length+len(words[used_id[id]])
				space_distrib=(maxWidth-length)/(len(used_id)-1)
				remain_count=(maxWidth-length)-space_distrib*(len(used_id)-1)
				for i in range(len(used_id)):
					line=line+words[used_id[i]]
					if i!=len(used_id)-1:
						line=line+' '*space_distrib
						if remain_count>0:
							line=line+' '
							remain_count=remain_count-1
			lines.append(line)
		return lines

s=Solution()
print s.fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."],30)