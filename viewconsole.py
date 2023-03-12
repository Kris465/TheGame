import os
import time

from Character import Character
from controller import Controller


class ViewConsole:
    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        self.display_info()
        while True:
            self.move()
    def display_info(self):
        field = self.controller.get_field()
        os.system("CLS")
        print("-" * 50)
        [print(i) for i in field.field]

    def move(self):
        try:
            move = int(input(f'1. Движение\n2. Атака\n3. Выход\n'))
            if int(move) == 1:
                move_side = int(input('1. Влево\n2. Вниз\n3. Вверх\n4. Вправо\n'))
                if 0 < move_side < 5:
                    self.controller.move(move_side)
                else:
                    self.validation()
            elif move == 2:
                self.damage(self.controller.attack())
            elif move == 3:
                exit()
            else:
                self.validation()
            self.controller.is_dead()
            self.display_info()
        except Exception as e:
            print(e)
            self.move()

    @staticmethod
    def validation():
        print("Ведено неверное значение")

    @staticmethod
    def damage(character: Character):
        if character is not None:
            print(f'{character.name} получил урон: {character.hp}')
        time.sleep(1)
