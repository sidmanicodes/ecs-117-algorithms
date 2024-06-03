from linked_list import LinkedList

def insertion_sort_linked_list(linked_list):
    # Return list if there is only one or no elemente
    if not linked_list.head or not linked_list.head.next:
        return linked_list
    
    # The end of the sorted part of the list (we consider the first element sorted)
    sorted_end = linked_list.head

    # As long as the sorted end of the list has a next node:
    while sorted_end.next:
        # If the node directly after the sorted part of the list is less than the end of the sorted part of the list,
        # move the node from the unsorted part to the correct position in the sorted part
        if sorted_end.next.data < sorted_end.data:
            # Detach the node
            copied_node = sorted_end.next
            sorted_end.next = copied_node.next

            # Find the insertion point
            # First, try seeing if we can insert in front of the head of the list (can potentially optimize solution)
            if copied_node.data < linked_list.head.data:
                copied_node.next = linked_list.head
                linked_list.head = copied_node
            # If that doesn't work, iterate through the sorted part of the list and find the insertion point
            else:
                cur = linked_list.head
                while cur.next != sorted_end.next and cur.next.data < copied_node.data:
                    cur = cur.next
                copied_node.next = cur.next
                cur.next = copied_node
        # Else, increment the end of the sorted part of the list (this node is sorted too)
        else:
            sorted_end = sorted_end.next

if __name__ == "__main__":
    my_list = LinkedList([5, 1, 3, 4])
    print(f"Before: {my_list}")
    insertion_sort_linked_list(my_list)
    print(f"After: {my_list}")
    