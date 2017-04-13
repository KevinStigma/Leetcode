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
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
		
class Solution(object):
	def swapPairs(self, head):
		if head==None or head.next==None:
			return head
		first=ListNode(-1)
		first.next=head
		pre=first
		ptr=head
		while ptr and ptr.next:
			node1=ptr
			node2=ptr.next
			node1.next=node2.next
			pre.next=node2
			node2.next=node1
			pre=node1
			ptr=node1.next
		return first.next
		
s=Solution()
printList(s.swapPairs(head))