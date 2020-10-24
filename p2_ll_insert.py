class Node:
	def __init__ (self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insertAfter(self, prev_node, new_data):
		if prev_node is None:
			print("Wrong Input")
			return
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def append(self,new_data):
		new_node = Node(new_data)
		last = self.head
		while (self.head):
			last = last.next
		
		last.next = new_node

	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next


if __name__== '__main__':
	llist = LinkedList()
	
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second
	second.next = third
	
	llist.printList()

	print("---------------------------")
	
	llist.push(4)
	
	llist.printList()

	print("---------------------------")

	llist.insertAfter(second, 5)

	llist.printList()