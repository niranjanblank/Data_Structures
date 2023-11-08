from typing import Type


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Data: {self.data} next: {self.next}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []

    def __str__(self):
        return f"Items: {self.items}"

    def __len__(self):
        return len(self.items)

    def append(self, node: Node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node


if __name__ == "__main__":
    linked_list = LinkedList()
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')

    linked_list.append(node1)
    linked_list.append(node2)
    linked_list.append(node3)
    linked_list.append(node4)
    item = linked_list.head

    while item.next:
        print(f"Current Data: {item.data}, Next Data: {item.next.data}")
        item = item.next
    else:
        print(f"Current Data: {item.data}, Next Data: {item.next}")
