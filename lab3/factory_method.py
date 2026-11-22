
class Warrior:
    def attack(self):
        print("Воин ударил мечом")


class Mage:
    def attack(self):
        print("Маг использовал заклинание")


class Creator:
    def create(self):
        pass

    def play(self):
        hero = self.create()
        hero.attack()


class WarriorCreator(Creator):
    def create(self):
        return Warrior()


class MageCreator(Creator):
    def create(self):
        return Mage()


warrior = WarriorCreator()
mage = MageCreator()

warrior.play()
mage.play()
