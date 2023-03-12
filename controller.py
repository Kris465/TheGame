from random import randint

from Character import CharacterAttack, CharacterReview, CharacterMove
from Field import Field
from Player import Player
from characters import Characters


class Controller:
    def __init__(self, characters: Characters, field: Field):
        self.characters = characters
        self.field = field
        self.init_units()

    def get_field(self):
        return self.field

    def get_characters(self):
        return self.characters.team

    def review(self):
        for ch in self.get_characters():
            ch.review_attr = CharacterReview(ch).review()

    def attack(self):
        self.review()
        for ch in self.get_characters():
            if isinstance(ch, Player):
                return CharacterAttack(ch).attack(self.get_characters())

    def is_dead(self):
        self.field_update()
        [self.get_characters().remove(ch) for ch in self.get_characters() if ch.hp <= 0]

    def move(self, move_side):
        self.review()
        for ch in self.get_characters():
            if isinstance(ch, Player):
                CharacterMove(ch).move(self.field, move_side)
                # ch.move(self.field, move_side, ch.review_attr)
        self.field_update()

    def field_update(self):
        for character in self.characters.team:
            place = character.place
            self.field.field[place[0]][place[1]] = character.sign

    def ran(self):
        return randint(0, self.field.size - 1)

    def generate(self):
        return [self.ran(), self.ran()]

    def init_units(self):
        for ch in self.characters.team:
            ch.place = self.generate()
            self.field.field[ch.place[0]][ch.place[1]] = ch.sign
