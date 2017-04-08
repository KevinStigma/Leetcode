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
head.next=ListNode(1)
# head.next.next=ListNode(2)
# head.next.next.next=ListNode(3)		
# head.next.next.next.next=ListNode(4)	
# head.next.next.next.next.next=ListNode(4)	
# head.next.next.next.next.next.next=ListNode(5)	
		
class Solution(object):
	def deleteDuplicates(self, head):
		if head==None:
			return head
		pre=ListNode(-1)
		pre.next=head
		ptr0=pre
		while ptr0.next:
			ptr1=ptr0.next
			if ptr1.next and ptr1.val==ptr1.next.val:
				ptr2=ptr1.next
				while ptr2 and ptr2.val==ptr1.val:
					ptr2=ptr2.next
				ptr0.next=ptr2
			else:
				ptr0=ptr1
		return pre.next
s=Solution()
printList(s.deleteDuplicates(head))
		