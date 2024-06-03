class LinkedList:
    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None
    def __init__(self, *args) -> None:
        self.head = None
        for arg in args:
            for item in arg:
                self.append(item)
    def append(self, data):
        new_node = self.Node(data=data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    def __str__(self) -> str:
        list_str = "["
        cur = self.head
        while cur.next:
            list_str += f"{cur.data} -> "
            cur = cur.next
        list_str += f"{cur.data}]"
        return list_str
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next