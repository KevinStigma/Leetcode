# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def printList(head):
	ptr=head
	while ptr!=None:
		print ptr.val
		ptr=ptr.next
		
head=ListNode(1)
# head.next=ListNode(4)
# head.next.next=ListNode(3)
# head.next.next.next=ListNode(2)		
# head.next.next.next.next=ListNode(5)	
# head.next.next.next.next.next=ListNode(2)	
class Solution(object):
	def partition(self, head, x):
		if head==None:
			return head
		min_greater=head.val
		pre=ListNode(-1)
		pre.next=head
		ptr=head
		ptr0=pre
		while ptr:
			if ptr.val>=x:
				break
			ptr=ptr.next
			ptr0=ptr0.next
		if ptr==None:
			return head
		while ptr.next:
			if ptr.next.val<x:
				tmp=ptr.next
				ptr.next=ptr.next.next
				tmp.next=ptr0.next
				ptr0.next=tmp
				ptr0=tmp
			else:
				ptr=ptr.next
		return pre.next
s=Solution()
printList(s.partition(head,2))