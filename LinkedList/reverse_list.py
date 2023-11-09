from LinkedList import LinkedList, Node


def reverse(linked_list):
    prev = None
    curr = linked_list.head
    next_node = None

    while curr:
        # store the next of current node to transverse the linked list
        next_node = curr.next
        # sett the next of current node to previous, initially the header will point to None
        curr.next = prev
        if not prev:
            # setting the tail of the linked list to point the initial header after changing its next to None
            linked_list.tail = curr
        # change the previous to current to store the address of the modified node which needs to be linked to the next
        # node in the original list
        prev = curr
        # set the current node to the previous saved next_node to transverse through the original list and make changes
        curr = next_node

    linked_list.head = prev

    return linked_list


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

    print(f'{"*" * 10} Reversing Linked List {"*" * 10}')
    reversed_list = reverse(linked_list)
    item = reversed_list.head

    while item.next:
        print(f"Current Data: {item.data}, Next Data: {item.next.data}")
        item = item.next
    else:
        print(f"Current Data: {item.data}, Next Data: {item.next}")
