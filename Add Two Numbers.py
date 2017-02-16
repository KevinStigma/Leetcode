class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		add=0
		start=ListNode(-1)
		pre_node=start
		while l1!=None or l2!=None:
			num1=num2=0
			if l1!=None:
				num1=l1.val
			if l2!=None:
				num2=l2.val
			sum=num1+num2+add
			add=sum//10
			cur_node=ListNode(sum%10)
			pre_node.next=cur_node
			pre_node=cur_node
			if l1!=None:
				l1=l1.next
			if l2!=None:
				l2=l2.next
		if add==1:
			cur_node=ListNode(1)
			pre_node.next=cur_node
		return start.next