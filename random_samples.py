# szimuláljuk na dobókockadobást 1-6

from random import randint, sample, shuffle
from secrets import choice

# a randint függvény nem built in függvény!
# a randint függvény a standard library része
number = randint(1, 7)
print(number)

numbers = [2, 4, 6, 8]
shuffle(numbers)
print(numbers)
cards = ["alsó", "felső", "király", "ász"]
card = choice(cards)
print(card)
print(sample(cards, k=2))