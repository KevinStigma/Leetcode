# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#1->2
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
def printList(head):
	ptr=head
	while ptr!=None:
		print ptr.val
		ptr=ptr.next

class Solution(object):
	def reorderList(self, head):
		count=0
		ptr=head
		if head==None or head.next==None:
			return None
		while ptr!=None:
			count=count+1
			ptr=ptr.next
		spilt_ind=count/2-1
		if count%2==1:
			spilt_ind=spilt_ind+1
		ptr=head
		for i in range(spilt_ind):
			ptr=ptr.next
		low_ptr=ptr
		high_ptr=ptr.next
		low_ptr.next=None
		low_ptr=head
		pre=high_ptr
		next=high_ptr.next
		pre.next=None
		while next!=None:
			high_ptr=next
			tmp=next.next
			next.next=pre
			pre=next
			next=tmp
		l1=low_ptr
		l2=high_ptr
		while l2!=None:
			next1=l1.next
			next2=l2.next
			l1.next=l2
			l2.next=next1
			l1=next1
			l2=next2

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
printList(head)
s=Solution()
s.reorderList(head)
			
		
		
		