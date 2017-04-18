# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
	def rotateRight(self, head, k):
		if head==None:
			return None
		fast=head
		slow=head
		n=0
		while fast!=None:
			n=n+1
			fast=fast.next
		k=k%n
		if k==0:
			return head
		fast=head
		for i in range(k):
			fast=fast.next
		while fast.next!=None:
			fast=fast.next
			slow=slow.next
		next=slow.next
		slow.next=None
		fast.next=head
		return next
		