import heapq

# TODO: REVER ISSO AQUI => ANOTAÇÃO PESQUISA K-PARES.
class Element:
    def __init__(self, id, features, path_img):
        self.id = id
        self.features = features
        self.path_img = path_img

    def __repr__(self):
        return f"Element(id={self.id}, path_img={self.path_img})"


class CustomHeap:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = 0

    def __str__(self):
        return str(self.heap)

    def add_item(self, a1: Element, a2: Element, distance=None):
        'Add a new item or update the priority of an existing item'
        item_id = (a1.id, a2.id)
        if item_id in self.entry_finder:
            self.remove_item(item_id)
        count = self.counter
        self.counter += 1
        entry = [count, (a1, a2, distance)]
        self.entry_finder[item_id] = entry
        heapq.heappush(self.heap, entry)

    def remove_item(self, item_id):
        'Mark an existing item as REMOVED. Raise KeyError if not found.'
        entry = self.entry_finder.pop(item_id)
        entry[-1] = self.REMOVED

    def pop_item(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.heap:
            count, item = heapq.heappop(self.heap)  # Unpack the entry into two variables.
            if item is not self.REMOVED:
                del self.entry_finder[(item[0].id, item[1].id)]
                return item
        raise KeyError('pop from an empty priority queue')