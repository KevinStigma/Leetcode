class Solution(object):
	def simplifyPath(self, path):
		if path[-1]=='/':
			index1=-1
			for i in range(len(path)-1,-1,-1):
				if path[i]!='/':
					index1=i
					break
			if index1==-1:
				return '/'
			index2=-1
			for i in range(index1-1,-1,-1):
				if path[i]=='/':
					index2=i
					break
			if index2==-1:
				return '/'+path[:index1+1]
			if path[index2+1:index1+1]!='..':
				path=path[:index1+1]
		path=path.replace('//','/')
		folders=path.split('/')
		last_slash_ind=-1
		normal_path=''
		for i in range(len(folders)):
			if folders[i]=='..':
				if normal_path!='':
					normal_path=normal_path[:last_slash_ind]
					for j in range(len(normal_path)-1,-1,-1):
						if normal_path[j]=='/':
							last_slash_ind=j
							break
			elif folders[i]!='' and folders[i]!='.':
				last_slash_ind=len(normal_path)
				normal_path=normal_path+'/'+folders[i]
		if normal_path=='':
			return '/'
		return normal_path
s=Solution()
print s.simplifyPath('/../')