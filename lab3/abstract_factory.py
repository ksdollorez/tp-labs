
class Sword:
    def use(self):
        print("Воин получил меч")


class Armor:
    def wear(self):
        print("Воин надел броню")


class Staff:
    def use(self):
        print("Маг получил посох")


class Robe:
    def wear(self):
        print("Маг надел мантию")


class WarriorItems:
    def create_weapon(self):
        return Sword()

    def create_armor(self):
        return Armor()


class MageItems:
    def create_weapon(self):
        return Staff()

    def create_armor(self):
        return Robe()


def give_items(factory):
    weapon = factory.create_weapon()
    armor = factory.create_armor()

    weapon.use()
    armor.wear()


give_items(WarriorItems())
give_items(MageItems())
