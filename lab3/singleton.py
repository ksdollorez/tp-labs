
class Game:
    _obj = None

    def __new__(cls):
        if cls._obj is None:
            cls._obj = super().__new__(cls)
            cls._obj.lives = 3
        return cls._obj


game = Game()

print("Жизней в начале игры:", game.lives)

game.lives -= 1
print("Игрок потерял жизнь")

new_game = Game()

print("Осталось жизней:", new_game.lives)
