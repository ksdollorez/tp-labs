
class Treasure:
    def open(self):
        print("Сокровищница открыта! Герой нашёл золото.")


class TreasureProxy:
    def __init__(self, has_key):
        self.has_key = has_key
        self.treasure = Treasure()

    def open(self):
        if self.has_key:
            self.treasure.open()
        else:
            print("Дверь закрыта. Нужен ключ.")

chest = TreasureProxy(False)
chest.open()

chest.has_key = True
chest.open()
