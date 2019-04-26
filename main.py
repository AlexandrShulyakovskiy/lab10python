import Ladder

FirstType_Ladder = Ladder.Ladder(maxLength = 5, producer = 'Triumph', maxMass = 7, price = 300, material = 'wood', colour = 'brown', condition = 'new')
SecondType_Ladder= Ladder.Ladder(maxLength = 10, producer = 'LvivDub', maxMass = 10, price = 500, material = 'metal', colour = 'silvery', condition = 'new')
ThirdType_Ladder = Ladder.Ladder(maxLength = 15, producer = 'CoolComp', maxMass = 13, price = 700, material = 'Carbon', colour = 'black', condition = 'new')

print(FirstType_Ladder)
print(SecondType_Ladder)
print(ThirdType_Ladder)