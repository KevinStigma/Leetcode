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
		parent=root
		begin=parent
		while begin!=None:
			while parent!=None and parent.left==None and parent.right==None:
				parent=parent.next
			if parent==None:
				begin=None
				continue
			cur_node=None
			if parent.left==None:
				begin=parent.right
				cur_node=parent.right
			elif parent.right==None:
				begin=parent.left
				cur_node=parent.left
			else:
				begin=parent.left
				cur_node=parent.right
				begin.next=cur_node
			parent=parent.next
			while parent!=None:
				if parent.left!=None:
					cur_node.next=parent.left
					cur_node=parent.left
				if parent.right!=None:
					cur_node.next=parent.right
					cur_node=parent.right
				parent=parent.next
			cur_node.next=None
			parent=begin