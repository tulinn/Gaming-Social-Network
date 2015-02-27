class Queue:
# first in first out

	def __init__(self):
		self.head = self.tail = None

	def isEmpty(self):
		# returns whether the queue is empty
		return not self.tail

	def enqueue(self, value):
		# adds value to the end of the queue
		if self.tail != None:
			prev = self.tail
			self.tail = LinkedListNode(value)
			prev.next = self.tail
		else:
			self.tail = LinkedListNode(value)
			self.head = self.tail

	def dequeue(self):
		"""
		>>> q = Queue()
		>>> q.enqueue(1)
		>>> print q.dequeue()
		1
		>>> print q.dequeue()
		None
		"""
		# removes and returns the first element in the queue
		if not self.head:
			return None # change with an exception
		value = self.head.value
		if not self.head.next:
			self.tail = self.head = None
		else:
			self.head = self.head.next
		return value

class LinkedListNode:
	def __init__(self, value=None, next=None):
		# Creating nodes with a value and a link to the next node
		self.value, self.next = value, next

	def __str__(self):
		# represents this node as a string
		return '(' + str(self.value) + ', ' + str(self.next) + ')' #recursive

if __name__ == "__main__":
	import doctest
	doctest.testmod()
