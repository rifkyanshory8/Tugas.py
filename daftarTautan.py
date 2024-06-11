class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def _init_(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Node sebelumnya yang diberikan tidak boleh kosong")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return temp
            temp = temp.next
        return None

    def delete_at_beginning(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next
        return temp.data

    def delete_at_end(self):
        if self.head is None:
            return None

        temp = self.head
        if temp.next is None:
            self.head = None
            return temp.data

        while temp.next.next is not None:
            temp = temp.next

        deleted_data = temp.next.data
        temp.next = None
        return deleted_data

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_beginning(5)
linked_list.insert_after(linked_list.head.next, 15)

print("Linked list:")
linked_list.print_list()

print("\nMencari node dengan nilai 15:")
found_node = linked_list.search(15)
if found_node:
    print("Node ditemukan:", found_node.data)
else:
    print("Node tidak ditemukan")

print("\nMenghapus node pertama:")
deleted_data = linked_list.delete_at_beginning()
print("Data yang dihapus:", deleted_data)
linked_list.print_list()

print("\nMenghapus node terakhir:")
deleted_data = linked_list.delete_at_end()
print("Data yang dihapus:", deleted_data)
