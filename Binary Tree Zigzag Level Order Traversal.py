# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def zigzagLevelOrder(self, root):
		if root==None:
			return []
		list=[[root.val]]
		queue=[]
		queue.append(root)
		queue2=[]
		queue2.append(0)
		cur_level=0
		while len(queue):
			l=[]
			while len(queue) and cur_level==queue2[0]:
				node=queue.pop(0)
				queue2.pop(0)
				if node.left!=None:
					queue.append(node.left)
					queue2.append(cur_level+1)
					l.append(node.left.val)
				if node.right!=None:
					queue.append(node.right)
					queue2.append(cur_level+1)
					l.append(node.right.val)
			if len(l):
				list.append(l[:])
			cur_level=cur_level+1
		new_list=[]
		for i in range(len(list)):
			if i%2==0:
				new_list.append(list[i][:])
			else:
				new_list.append(list[i][::-1])
		return new_list
		
		
		