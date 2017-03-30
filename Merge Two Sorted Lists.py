# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def printList(head):
	ptr=head
	while ptr:
		print ptr.val
		ptr=ptr.next
		
class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if l1==None and l2==None:
			return None
		if l1==None:
			return l2
		elif l2==None:
			return l1
		s_head=None
		b_head=None
		if l1.val>l2.val:
			s_head=l2
			b_head=l1
		else:
			s_head=l1
			b_head=l2
		while b_head:
			ptr=s_head
			while ptr.next:
				if ptr.next.val>b_head.val:
					break
				ptr=ptr.next
			s_head=b_head
			b_head=ptr.next
			ptr.next=s_head
		if l1.val<=l2.val:
			return l1
		else:
			return l2
a=ListNode(1)
a.next=ListNode(3)
a.next.next=ListNode(5)
b=ListNode(2)
b.next=ListNode(4)
b.next.next=ListNode(6)
s=Solution()
printList(s.mergeTwoLists(a,b))