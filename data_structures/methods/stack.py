# https://www.geeksforgeeks.org/stack-in-python/
"""
maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking.
qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull.

others, size, push (put element on top of array), pop (delete first element), peek (get first element),

"""


class Stack:
	stack = []

	def get_size(self):
		return len(self.stack)

	def is_empty(self):
		return self.get_size() == 0

	def peek(self):
		return self.stack[0]