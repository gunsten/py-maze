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
        if value is None:
            raise ValueError("Cannot add None element to LinkedList")
        self.head = value
        self.tail = linked_list

    @property
    def has_tail(self):
        return self.tail is not None

    @property
    def is_empty(self):
        return self.head is None

    def to_list(self):
        if not self.has_tail:
            return []
        as_list = [self.head]
        cursor = self.tail
        while not cursor.is_empty and cursor is not None:
            as_list.append(cursor.head)
            cursor = cursor.tail
        return as_list

    def __repr__(self):
        return self.to_list().__repr__()

    @staticmethod
    def empty():
        return LinkedList()

    @staticmethod
    def cons(element, linked_list=None):
        if linked_list is None or linked_list.is_empty:
            return LinkedList(element)
        return LinkedList(element, linked_list)