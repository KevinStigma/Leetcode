# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution(object):
	def copyRandomList(self, head):
		if head==None:
			return None
		new_head=RandomListNode(head.label)
		ptr=head
		pre=new_head
		map={}
		map[ptr]=pre
		map[None]=None
		while ptr!=None:
			ptr=ptr.next
			if ptr==None:
				pre.next=None
				break
			node=RandomListNode(ptr.label)
			pre.next=node
			pre=node
			map[ptr]=pre
		ptr=head
		new_ptr=new_head
		while ptr!=None:
			new_ptr.random=map[ptr.random]
			ptr=ptr.next
			new_ptr=new_ptr.next
		return new_head

			
			
			
			
			
		