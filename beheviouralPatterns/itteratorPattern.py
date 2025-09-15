from collections.abc import Iterable, Iterator


# iterator interface
class listIterator(Iterator):
    def __init__(self, items):
        self._collection = items
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        raise StopIteration


# aggregate interface
class listAggregate(Iterable):
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return listIterator(self._items)


# client code
if __name__ == "__main__":
    aggregate = listAggregate()
    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

    for item in aggregate:
        print(item)
