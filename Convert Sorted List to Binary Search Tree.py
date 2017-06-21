# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def getMidNode(head,end):
	if head==None or head==end:
		return None
	fast=head
	low=head
	while fast!=end:
		fast=fast.next
		if fast!=end:
			fast=fast.next
			low=low.next
	return low
		
class Solution(object):
	def listToBST(self,head,end):
		mid=getMidNode(head,end)
		if mid==None:
			return None
		root=TreeNode(mid.val)
		root.right=self.listToBST(mid.next,end)
		root.left=self.listToBST(head,mid)
		return root
	def sortedListToBST(self, head):
		if head==None:
			return None
		return self.listToBST(head,None)