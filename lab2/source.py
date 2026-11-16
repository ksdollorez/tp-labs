from abc import ABC, abstractmethod

class GameObject:
    def __init__(self, object_id: int, name: str, x: int, y: int):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def getId(self) -> int:
        return self._id

    def getName(self) -> str:
        return self._name

    def getX(self) -> int:
        return self._x

    def getY(self) -> int:
        return self._y


class Unit(GameObject):
    def __init__(self, object_id: int, name: str, x: int, y: int, hp: float):
        super().__init__(object_id, name, x, y)
        self._hp = max(0.0, hp)

    def isAlive(self) -> bool:
        return self._hp > 0

    def getHp(self) -> float:
        return self._hp

    def receiveDamage(self, damage: float) -> None:
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")
        self._hp = max(0.0, self._hp - damage)


class Building(GameObject):
    def __init__(self, object_id: int, name: str, x: int, y: int, built: bool):
        super().__init__(object_id, name, x, y)
        self._built = built

    def isBuilt(self) -> bool:
        return self._built


class Attacker(ABC):
    @abstractmethod
    def attack(self, target: Unit) -> None:
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass


class Archer(Unit, Attacker, Moveable):
    def attack(self, target: Unit) -> None:
        if self.isAlive():
            target.receiveDamage(20.0)

    def move(self, x: int, y: int) -> None:
        if self.isAlive():
            self._x = x
            self._y = y


class Fort(Building, Attacker):
    def attack(self, target: Unit) -> None:
        if self.isBuilt():
            target.receiveDamage(35.0)


class MobileHouse(Building, Moveable):
    def move(self, x: int, y: int) -> None:
        self._x = x
        self._y = y