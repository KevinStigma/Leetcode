class Solution:
    def subsetsWithDup(self, S):
        # write your code here
        S.sort()
        p = [[S[x] for x in range(len(S)) if i>>x&1] for i in range(2**len(S))]
        func = lambda x,y:x if y in x else x + [y]
        p = reduce(func, [[], ] + p)
        return list(reversed(p))
		
s=Solution()
print s.subsetsWithDup([1,2,2])
		