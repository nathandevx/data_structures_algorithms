# Resource: https://github.com/M2skills/Linked-List-in-Python
# temp, cur,
# if not cur (if cur is not none), while cur (while cur is not none)
# Other methods: remove_last(),

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return f'{self.data}'


class LinkedList:
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head is None

	def length(self):
		cur = self.head
		if not cur:
			return 0
		counter = 0
		while cur:
			counter += 1
			cur = cur.next
		return counter

	def display(self):
		cur = self.head
		while cur:
			print(f'{cur.data} ', end="")
			cur = cur.next

	def insert_start(self, new_data):  # add to start of list
		new_node = Node(new_data)
		new_node.next, self.head = self.head, new_node

	def insert_end(self, new_data):  # add to end of list
		cur = self.head
		new_node = Node(new_data)
		if not cur:
			self.head = new_node
			return
		while cur.next:  # when there's not something next, break the loop and make that next the new node
			cur = cur.next
		cur.next = new_node  # the next node (nonexistent) is equal to the new node

	def insert_after(self, prev_node, new_data):
		new_node = Node(new_data)
		new_node.next, prev_node.next = prev_node.next, new_node

	def insert(self, new_data, pos):  # add element at given position
		if pos < 1:
			print("Invalid position. Using insert_start() method to insert element at beginning of list.")
			return
		new_node = Node(new_data)
		cur = self.head
		counter = 1
		while cur:
			if counter == pos:
				new_node.next, cur.next = cur.next, new_node
				return
			counter += 1
			cur = cur.next

	def remove_first(self):
		self.head = self.head.next

	def remove_last(self):
		cur = self.head
		prev = None
		while cur.next:
			prev = cur
			cur = cur.next
		prev.next = None

	def remove(self, pos):
		cur = self.head
		if pos < 1:
			print("Use remove_first() method")
			return
		counter = 1
		while cur:
			if counter == pos:
				cur.next = cur.next.next
				return
			counter += 1
			cur = cur.next
		return cur

	def search(self, item):
		cur = self.head
		while cur:
			if cur.data == item:
				return True
			cur = cur.next
		return False

	def reverse(self):
		prev = None
		cur = self.head
		while cur:
			temp = cur
			cur.next, cur = cur, prev
			prev = temp
			cur = cur.next
			# next = cur.next
			# cur.next = prev
			# prev = cur
			# cur = next
		# self.head = prev

	def sort(self, head):
		current = head
		index = Node(None)

		if head is None:
			return
		else:
			while current is not None:
				# index points to the node next to current
				index = current.next

				while index is not None:
					if current.data > index.data:
						current.data, index.data = index.data, current.data

					index = index.next
				current = current.next

	def is_sorted(self):
		cur = self.head
		while cur:
			if cur.next:  # is there a next node
				if cur.data > cur.next.data:
					return False
			cur = cur.next
		return True


if __name__ == '__main__':
	linked_list = LinkedList()
	linked_list.head = Node(1)
	linked_list.head.next = Node(2)
	linked_list.head.next.next = Node(3)
	linked_list.head.next.next.next = Node(4)

	linked_list.display()
	print()
	linked_list.reverse()
	linked_list.display()
