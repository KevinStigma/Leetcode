# Definition for singly-linked list.
import os
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
head.next.next=ListNode(3)
head.next.next.next=ListNode(5)	

head.next.next.next.next=ListNode(7)	
head.next.next.next.next.next=ListNode(2)	
head.next.next.next.next.next.next=ListNode(4)	
head.next.next.next.next.next.next.next=ListNode(6)	

class Solution(object):
	def splitLinkFromMiddle(self,head):
		fast=head
		slow=head
		while not(fast.next==None):
			fast=fast.next
			if fast.next==None:
				break
			fast=fast.next
			slow=slow.next
		new_link=slow.next	
		slow.next=None
		return [head,new_link]
		
	def merge2SortedLinks(self,l1,l2):
		if l1==None:
			return l2
		elif l2==None:
			return l1
		ptr1=None
		ptr2=None
		if l1.val<l2.val:
			ptr1=l1
			ptr2=l2
		else:
			ptr1=l2
			ptr2=l1
		head=ptr1
		while ptr2!=None:
			while ptr1.next!=None:
				if ptr1.next.val<=ptr2.val:
					ptr1=ptr1.next
				else:
					break
			tmp=ptr1.next
			ptr1.next=ptr2
			ptr1=ptr2
			ptr2=tmp
		return head
	def mergeSort(self,head):
		if head==None or head.next==None:
			return head
		[l1,l2]=self.splitLinkFromMiddle(head)		
		l1=self.mergeSort(l1)
		l2=self.mergeSort(l2)
		l3=self.merge2SortedLinks(l1,l2)
		return l3
		
	def sortList(self, head):
		return self.mergeSort(head)
		
s=Solution()
printList(s.sortList(head))