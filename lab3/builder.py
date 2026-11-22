
class Hero:
    def __init__(self, name, hero_class, weapon):
        self.name = name
        self.hero_class = hero_class
        self.weapon = weapon

    def show(self):
        print("Имя:", self.name)
        print("Класс:", self.hero_class)
        print("Оружие:", self.weapon)


class HeroBuilder:
    def __init__(self):
        self.name = ""
        self.hero_class = ""
        self.weapon = ""

    def set_name(self, name):
        self.name = name
        return self

    def set_class(self, hero_class):
        self.hero_class = hero_class
        return self

    def set_weapon(self, weapon):
        self.weapon = weapon
        return self

    def build(self):
        return Hero(self.name, self.hero_class, self.weapon)


builder = HeroBuilder()

hero1 = (builder
         .set_name("Артур")
         .set_class("Воин")
         .set_weapon("Меч")
         .build())

hero2 = (builder
         .set_name("Мерлин")
         .set_class("Маг")
         .set_weapon("Посох")
         .build())

print("Первый герой:")
hero1.show()

print("\nВторой герой:")
hero2.show()
