# Resource: https://github.com/M2skills/Linked-List-in-Python
# temp, cur,
# if not cur (if cur is not none), while cur (while cur is not none)
# Other methods: remove_last(),

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


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
		while cur.next:
			cur = cur.next
		cur.next = new_node

	def insert_after(self, prev_node, new_data):
		new_node = Node(new_data)
		new_node.next, prev_node.next = prev_node.next, new_node

	def insert(self, new_data, pos):  # add element at given position
		if pos < 1:
			print("Invalid position. Using insert_start() method to insert element at beginning of list.")
			return
		new_node = Node(new_data)
		cur = self.head
		counter = 0
		while cur:
			if counter == pos:
				new_node.next, cur.next = cur.next, new_node
				return
			counter += 1
			cur = cur.next

	def remove_last(self):
		prev = None
		cur = self.head
		while cur.next is not None:
			prev = cur
			cur = cur.next

	def remove(self, position):  # delete element at given position
		if self.head is None:
			return
		temp = self.head
		if position == 0:
			self.head = temp.next
			temp = None
			return

		# Find the key to be deleted
		for i in range(position - 1):
			temp = temp.next
			if temp is None:
				break

		# If the key is not present
		if temp is None:
			return
		if temp.next is None:
			return

		next = temp.next.next
		temp.next = None
		temp.next = next

	def search(self, key):
		current = self.head
		while current is not None:
			if current.data == key:
				return True
			current = current.next
		return False

	def reverse(self):  # reverse list
		prev = None
		current = self.head
		while current is not None:
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	def sort(self, head):  # sort list
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

	def is_sorted(self):  # is list sorted?
		cur = self.head
		while None not in [cur, cur.next]:
			if cur.next is not None:
				if cur.data > cur.next.data:
					return False
			cur = cur.next
		return True


if __name__ == '__main__':
	linked_list = LinkedList()
	linked_list.head = Node(1)
	linked_list.head.next = Node(2)
	linked_list.head.next.next = Node(5)
	linked_list.head.next.next.next = Node(7)

	linked_list.display()
	print()
	linked_list.insert(4, 0)
	linked_list.display()
