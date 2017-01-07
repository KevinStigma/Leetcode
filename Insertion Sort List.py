#This question is difficult for me, mark it
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
		
def printList(head):
	node=head
	while node!=None:
		print node.val
		node=node.next

head=ListNode(3)
s1=ListNode(2)
head.next=s1
s2=ListNode(1)
s1.next=s2
s3=ListNode(9)
s2.next=s3
s4=ListNode(6)
s3.next=s4
s5=ListNode(10)
s4.next=s5
		
class Solution(object):
	def insertionSortList(self, head):
		if head is None or head.next is None:  
			return head  
		dummyNode=ListNode(0)
		dummyNode.next=head
		
		cur_node=head
		while cur_node.next:
			if cur_node.val>cur_node.next.val:
				pre=dummyNode
				while pre.next.val<cur_node.next.val:
					pre=pre.next
				moved_node=cur_node.next
				cur_node.next=moved_node.next
				moved_node.next=pre.next
				pre.next=moved_node
			else:
				cur_node=cur_node.next
		return dummyNode.next
			
s=Solution()
head=s.insertionSortList(head)
printList(head)