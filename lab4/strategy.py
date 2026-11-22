class Sword:
    def attack(self):
        print("Герой ударил мечом")


class Magic:
    def attack(self):
        print("Герой использовал магию")


class Hero:
    def __init__(self, weapon):
        self.weapon = weapon

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        self.weapon.attack()


hero = Hero(Sword())
hero.attack()

hero.change_weapon(Magic())
hero.attack()