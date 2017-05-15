# Definition for binary tree with next pointer.
class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	def connect(self, root):
		if root==None:
			return
		root.next=None
		begin=root
		while not(begin.left==None or begin.right==None):
			cur_node=begin
			pre=None
			while cur_node!=None:
				cur_node.left.next=cur_node.right
				if pre!=None:
					pre.right.next=cur_node.left
				pre=cur_node
				cur_node=cur_node.next
			pre.right=None
			begin=begin.left