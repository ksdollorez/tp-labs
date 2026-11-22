
class Hero:
    def __init__(self):
        self.name = ""
        self.hero_class = ""
        self.weapon = ""

    def show(self):
        print("Имя:", self.name)
        print("Класс:", self.hero_class)
        print("Оружие:", self.weapon)


class HeroBuilder:
    def __init__(self):
        self.hero = Hero()

    def set_name(self, name):
        self.hero.name = name
        return self

    def set_class(self, hero_class):
        self.hero.hero_class = hero_class
        return self

    def set_weapon(self, weapon):
        self.hero.weapon = weapon
        return self

    def build(self):
        return self.hero


builder = HeroBuilder()

hero = (builder
        .set_name("Артур")
        .set_class("Воин")
        .set_weapon("Меч")
        .build())

hero.show()
