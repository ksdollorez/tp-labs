
class Heal:
    def __init__(self, limit, name, next_heal=None):
        self.limit = limit
        self.name = name
        self.next_heal = next_heal

    def handle(self, hp):
        if hp >= self.limit:
            print("Использовано:", self.name)
            return

        if self.next_heal is not None:
            self.next_heal.handle(hp)
        else:
            print("Подходящего лечения нет")


healer = Heal(0, "Целитель")
big = Heal(30, "Большое зелье", healer)
small = Heal(70, "Малое зелье", big)

print("Здоровье героя: 85")
small.handle(85)

print("Здоровье героя: 50")
small.handle(50)

print("Здоровье героя: 10")
small.handle(10)
