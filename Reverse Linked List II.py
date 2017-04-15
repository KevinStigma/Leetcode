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

#1->2->3->4->5
		
class Solution(object):
	def reverseBetween(self, head, m, n):
		if head==None:
			return head
		if m==n:
			return head
		begin=head
		end=head
		first=ListNode(-1)
		first.next=head
		pre=first
		for i in range(m-1):
			pre=pre.next
			begin=begin.next
			end=end.next
		for i in range(n-m):
			end=end.next
		next=end.next
		ptr=begin.next
		ptr0=begin
		while ptr!=next:
			tmp=ptr.next
			ptr0.next=ptr.next
			ptr.next=pre.next
			pre.next=ptr
			ptr=tmp
		return first.next
s=Solution()
printList(s.reverseBetween(head,2,4))