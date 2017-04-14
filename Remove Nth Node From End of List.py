# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		if head==None:
			return head
		fast=head
		slow=head
		for i in range(n):
			fast=fast.next
		if fast==None:
			return head.next
		pre=slow
		while fast:
			fast=fast.next
			if slow!=pre:
				pre=pre.next
			slow=slow.next
		pre.next=slow.next
		return head
		
		