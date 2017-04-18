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
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(6)
				
class Solution(object):
	def reverseKGroup(self, head, k):
		if head==None or head.next==None:
			return head
		if k==1:
			return head
		first=ListNode(-1)
		first.next=head
		pre=first
		while pre.next:
			begin=pre.next
			ptr=begin
			for i in range(k-1):
				ptr=ptr.next
				if ptr==None:
					return first.next
			end=ptr.next
			ptr=begin.next
			while ptr!=end:
				tmp=ptr.next
				ptr.next=pre.next
				pre.next=ptr
				ptr=tmp
			begin.next=ptr
			pre=begin
		return first.next
s=Solution()
printList(s.reverseKGroup(head,2))