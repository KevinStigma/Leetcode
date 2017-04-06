# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		if head==None:
			return head
		ptr1=head
		while ptr1:
			ptr2=ptr1.next
			while ptr2 and ptr2.val==ptr1.val:
				ptr2=ptr2.next
			ptr1.next=ptr2	
			ptr1=ptr1.next
		return head
		
		