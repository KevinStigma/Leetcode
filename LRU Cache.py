class ListNode(object):
	def __init__(self, k,v):
		self.key = k
		self.val= v
		self.next = None
		self.pre = None
	
class LRUCache(object):
	def __init__(self, capacity):
		self.root=ListNode(-1,-1)
		self.root.next=self.root
		self.root.pre=self.root
		self.capacity=capacity
		self.size=0
		self.maps={}
	def get(self, key):
		if not(key in self.maps):
			return -1
		node=self.maps[key]
		if self.size==1:
			return node.val
		last_node=node.next
		pre_node=node.pre
		last_node.pre=pre_node
		pre_node.next=last_node
		
		head_node=self.root.next
		self.root.next=node
		node.next=head_node
		node.pre=self.root
		head_node.pre=node
		return node.val
		
	def put(self, key, value):
		node=None
		if key in self.maps:
			node=self.maps[key]
			node.val=value
			last_node=node.next
			pre_node=node.pre
			pre_node.next=last_node
			last_node.pre=pre_node
		else:
			node=ListNode(key,value)
		head_node=self.root.next
		self.root.next=node
		node.next=head_node
		node.pre=self.root
		head_node.pre=node
		if key in self.maps:
			return
		self.maps[key]=node
		if self.size==self.capacity:
			tail_node=self.root.pre
			last_node=tail_node.pre
			self.root.pre=last_node
			last_node.next=self.root
			del self.maps[tail_node.key]
		else:
			self.size=self.size+1
		
# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
print cache.get(2)
cache.put(1, 1)
cache.put(4, 1)
print cache.get(2)