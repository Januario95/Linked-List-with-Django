class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.head


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for cur_node in self:
            pass
        cur_node.next = node

    def add_after(self, target, new_node):
        self.check_head()

        for node in self:
            if node.data == target:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception('Node with data %s not found' % target)

    def add_before(self, target, new_node):
        self.check_head()

        if self.head.data == target:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found." % target)

    def remove_node(self, target):
        self.check_head()

        if self.head.data == target:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target:
                prev_node.next = node.next
                return
            prev_node = node

    def check_head(self):
        if self.head is None:
            raise Exception('List is empty')
