import os


class ViewConsole:
    @staticmethod
    def display_info(field):
        os.system("CLS")
        print("-" * 50)
        [print(i) for i in field.field]

    @staticmethod
    def move():
        return int(input(f'1. Движение\n2. Атака\n'))

    @staticmethod
    def movement():
        return int(input(
            '1. Влево\n2. Вниз\n3. Вверх\n4. Вправо\n'
        ))
