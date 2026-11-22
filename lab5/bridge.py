
class Sword:
    def use(self):
        print("ударил мечом")


class Staff:
    def use(self):
        print("использовал посох")


class Hero:
    def __init__(self, weapon):
        self.weapon = weapon

    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        print("Воин", end=" ")
        self.weapon.use()


class Mage(Hero):
    def attack(self):
        print("Маг", end=" ")
        self.weapon.use()

warrior = Warrior(Sword())
mage = Mage(Staff())

warrior.attack()
mage.attack()

warrior.weapon = Staff()
warrior.attack()
