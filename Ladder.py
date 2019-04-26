class Ladder:

    numberOfLaddersPurchased = 0

    def __init__(self, maxLength = 0, producer = None, maxMass = 0, price = 0, material = None, colour = None, condition = None):
        self.maxLength = maxLength
        self.producer = producer
        self.maxMass  = maxMass 
        self.price = price
        self.material = material
        self.colour = colour
        self.condition = condition

        Ladder.numberOfLaddersPurchased += 1

    def __del__(self):
        print('Ladder {} deleted'.format(self.maxLength))

    @staticmethod
    def get_numberOfLaddersPurchased():
        return Ladder.numberOfLaddersPurchased

    def __str__(self):
        return ('maxLength= {} m, producer = {}, maxMass = {} kg, price = {} $, material = {}, colour = {}, condition = {}').format(self.maxLength, self.producer, self.maxMass, self.price, self.material, self.colour, self.condition)

