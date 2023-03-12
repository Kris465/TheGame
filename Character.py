import random

from move import Move


class Character:
    @property
    def name(self) -> int:  # возможно тут надо стринг
        return self._name

    @property
    def full_hp(self) -> int:
        return self._base_hp

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def attack_power(self) -> int:
        return self._attack

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, item):
        self._place = item

    @property
    def sign(self):
        return self._sign

    def __init__(self, character) -> None:
        self._name = '' if character._name is None else character._name
        self._base_hp = character._hp
        self._hp = self._base_hp
        self._attack = character._attack
        self._sign = character._sign
        self._step = character._step
        self._place = None
        self.review_attr = None


class CharacterMove:
    def __init__(self, character: Character):
        self.character = character

    def _move_side(self, field, pos_cur, pos_new):
        if 0 <= pos_new[0] <= field.size - 1 and 0 <= pos_new[1] <= field.size - 1:
            field.field[pos_new[0]][pos_new[1]] = self.character.sign
            field.field[pos_cur[0]][pos_cur[1]] = '-'
            self.character._place = pos_new
        else:
            field.field[pos_cur[0]][pos_cur[1]] = self.character.sign
        return field

    def move(self, field, move: int):
        match move:
            case Move.LEFT.value:
                return self._move_side(field, self.character.review_attr['cp'], self.character.review_attr['left'])
            case Move.DOWN.value:
                return self._move_side(field, self.character.review_attr['cp'], self.character.review_attr['down'])
            case Move.UP.value:
                return self._move_side(field, self.character.review_attr['cp'], self.character.review_attr['up'])
            case Move.RIGHT.value:
                return self._move_side(field, self.character.review_attr['cp'], self.character.review_attr['right'])


class CharacterReview:
    def __init__(self, character: Character):
        self.character = character

    def review(self) -> dict:
        step = self.character._step
        cp = {}
        x, y = self.character._place
        cp['cp'] = self.character._place
        cp['left'] = [x, y - step]
        cp['down'] = [x + step, y]
        cp['up'] = [x - step, y]
        cp['right'] = [x, y + step]
        return cp


class CharacterAttack:
    def __init__(self, character: Character):
        self.character = character

    def attack(self, characters: list) -> Character:
        damage = random.randint(0, self.character.attack_power)
        for character in characters:
            for key, value in self.character.review_attr.items():
                if key != 'cp' and self.character.review_attr[key] == character.place:
                    return self._get_damage(character, damage)
        return None

    def _get_damage(self, character: Character, damage: int) -> Character:
        character._hp -= damage
        if character._hp <= 0:
            character._sign = '-'
        return character
