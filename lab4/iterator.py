
class ItemIterator:
    def __init__(self, items):
        self.items = tuple(items)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration

        item = self.items[self.index]
        self.index += 1
        return item


class Inventory:
    def __init__(self, items):
        self.items = list(items)

    def __iter__(self):
        return ItemIterator(self.items)


bag = Inventory(["Меч", "Зелье", "Ключ"])

print("Предметы в инвентаре:")
for item in bag:
    print(item)

print("Проверяем инвентарь ещё раз:")
for item in bag:
    print(item)
