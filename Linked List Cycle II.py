class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def detectCycle(self, head):
		if head==None or head.next==None:
			return None
		if head.next==head:
			return head 
		slow=head
		fast=head
		while fast.next:
			slow=slow.next
			fast=fast.next.next
			if fast==None:
				return None
			if fast==slow:
				break
		if fast.next==None:
			return None
		slow=head
		while slow!=fast:
			fast=fast.next
			slow=slow.next
		return slow
		