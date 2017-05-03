# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		cur_ind=0
	def preOrder(self,root,list):
		if root!=None:
			list.append(root.val)
			self.preOrder(root.left,list)
			self.preOrder(root.right,list)
	def rebuild(self,in_list,post_list,begin_id,end_id,root_val):
		if begin_id>end_id:
			return
		root_ind=begin_id
		for i in range(begin_id,end_id+1):
			if in_list[i]==root_val:
				root_ind=i
				break
		root=TreeNode(root_val)
		self.cur_ind=self.cur_ind-1
		if self.cur_ind<0:
			return root
		right_child=self.rebuild(in_list,post_list,root_ind+1,end_id,post_list[self.cur_ind])
		root.right=right_child
		if self.cur_ind<0:
			return root
		left_child=self.rebuild(in_list,post_list,begin_id,root_ind-1,post_list[self.cur_ind])
		root.left=left_child
		return root
		
	def buildTree(self, p, q):
		in_list=p
		post_list=q
		self.cur_ind=len(post_list)-1
		if len(post_list)==0:
			return []
		if len(post_list)==1:
			root=TreeNode(post_list[0])
			return root
		return self.rebuild(in_list,post_list,0,len(post_list)-1,post_list[-1])
s=Solution()
root=s.buildTree([4,2,5,1,3],[4,5,2,3,1])
list=[]
print root.left.val
print root.right.val
s.preOrder(root,list)
print list