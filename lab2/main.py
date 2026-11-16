from source import Archer, Fort, MobileHouse, Unit


def main():
    archer = Archer(1, "Лучник", 0, 0, 100.0)
    target = Unit(2, "Цель", 1, 1, 100.0)
    fort = Fort(3, "Крепость", 2, 2, True)
    house = MobileHouse(4, "Дом на колёсах", 0, 0, True)

    archer.move(3, 4)
    print("Координаты лучника:", archer.getX(), archer.getY())

    archer.attack(target)
    print("Здоровье цели после атаки лучника:", target.getHp())

    fort.attack(target)
    print("Здоровье цели после атаки крепости:", target.getHp())

    house.move(5, 6)
    print("Координаты дома:", house.getX(), house.getY())


if __name__ == "__main__":
    main()