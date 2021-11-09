class LinkedList:
    def __init__(self, value=None, linked_list=None):
        if value is None and linked_list is None:
            self.head = None
            self.tail = None
            return
        if linked_list is None:
            self.head = value
            self.tail = LinkedList()
            return
        self.head = value
        self.tail = linked_list

    @property
    def has_tail(self):
        return self.tail is not None

    @property
    def is_empty(self):
        return self.tail is None

    def to_list(self):
        return [e for e in self]

    def __repr__(self):
        return self.to_list().__repr__()

    def __iter__(self):
        cursor = self
        while not cursor.is_empty:
            yield cursor.head
            cursor = cursor.tail

    def __eq__(self, other):
        if self is other:
            return True

        cursor_s, cursor_o = self, other

        while True:
            if cursor_s is cursor_o:
                return True
            if cursor_s.is_empty and cursor_o.is_empty:
                return True
            if cursor_s.is_empty:
                return False
            if cursor_o.is_empty:
                return False
            if cursor_s.head != cursor_o.head:
                return False
            cursor_s, cursor_o = cursor_s.tail, cursor_o.tail


def empty_list() -> LinkedList:
    return LinkedList()


def cons(element, linked_list) -> LinkedList:
    return LinkedList(element, linked_list)
