class node:
    def __init__(self,data):
        self.data = data
        self.next_node = None


class linked_list:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self,data):
        new_node = node(data)
        if self.is_empty():
            self.head = new_node

        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next_node
        print(" -> ".join(map(str,elements)))

        
my_linked_list = linked_list()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print("linked list: ")
my_linked_list.display()