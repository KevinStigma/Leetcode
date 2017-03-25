# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def hasCycle(self, head):
		if head==None or head.next==None:
			return False 
		slow=head
		fast=head.next
		if fast==slow:
			return True
		while 1:
			slow=slow.next
			for i in range(2):
				fast=fast.next
				if fast==slow:
					return True
				elif fast==None:
					return False
		return False
	
s=Solution()