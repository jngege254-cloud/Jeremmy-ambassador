class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Add element to end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Add element to beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at specific position
    def insert_at_position(self, data, pos):
        new_node = Node(data)

        if pos == 0:
            self.prepend(data)
            return

        temp = self.head
        count = 0

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if not temp:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete first occurrence of value
    def delete_by_value(self, value):
        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if not temp:
            print("Value not found")
            return

        prev.next = temp.next

    # Search for value (return index or -1)
    def search(self, value):
        temp = self.head
        index = 0

        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1

        return -1

    # Display all elements
    def display(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Check if list is empty
    def is_empty(self):
        return self.head is None

    # Return number of nodes
    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


# Example usage
ll = SinglyLinkedList()

ll.append(10)
ll.append(20)
ll.prepend(5)
ll.insert_at_position(15, 2)

ll.display()  # 5 -> 10 -> 15 -> 20 -> None

print("Search 15:", ll.search(15))  # index
print("Size:", ll.size())

ll.delete_by_value(10)
ll.display()

print("Is empty:", ll.is_empty())