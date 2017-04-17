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
head.next.next=ListNode(3)
head.next.next.next=ListNode(5)	

head1=ListNode(2)
head1.next=ListNode(4)
head1.next.next=ListNode(6)
head1.next.next.next=ListNode(8)	
		
head3=ListNode(3)
head3.next=ListNode(9)
head3.next.next=ListNode(10)
head3.next.next.next=ListNode(12)		
		
class Solution(object):
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
	def mergeKLists(self, lists):
		n=len(lists)
		if n==0:
			return None
		elif n==1:
			return lists[0]
		elif n==2:
			return self.merge2SortedLinks(lists[0],lists[1])
		mid=n/2	
		l1=self.mergeKLists(lists[0:mid+1])
		l2=self.mergeKLists(lists[mid+1:])
		return self.merge2SortedLinks(l1,l2)
s=Solution()
printList(s.mergeKLists([head,head1,head3]))