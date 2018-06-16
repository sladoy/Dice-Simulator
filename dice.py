from random import randint

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        self.number_of_dices = 0
        self.number_of_dice_rolls = 0
        self.current_number_of_dice_rolls = 0
        self.max_sides = 0

    def roll(self):
        return randint(1, self.num_sides)

    def generate_labels(self):
        lista = []

        for number in range(self.number_of_dices, self.max_sides + 1):
            lista.append(number)

        return lista

    def generate_frequencies(self, results):
        frequencies = []
        self.max_sides = self.num_sides * self.number_of_dices
        for value in range(self.number_of_dices, self.max_sides + 1):
            freq = results.count(value)
            frequencies.append(freq)

        return frequencies

    def generate_results(self, throw_value, dice_value):
        results = []
        result = 0
        self.number_of_dice_rolls = throw_value
        self.number_of_dices = dice_value

        for x in range(1, self.number_of_dice_rolls + 1):
            for y in range(1, self.number_of_dices + 1):
                result += Die.roll(self)
            results.append(result)
            result = 0
        return results

    def generate_dies(self):
        d = str(self.number_of_dices) + 'x' + ' D' + str(self.num_sides)
        return d

    def generate_sides(self, side_value):
        self.num_sides = side_value
