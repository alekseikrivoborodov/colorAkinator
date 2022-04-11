import random
from autocorrect import Speller

spell = Speller(lang='en')

print(spell('mussage'))
print(spell('survice'))
print(spell('hte'))

print(random.randint(0, 12))
random_choise = random.choice("КФРБЧС")

color = "Красный, Фиолетовый, Розовый, Белый, Черный, Серый,"

if random_choise in color:
    print(random_choise)
    index_letter = color.index(random_choise)
    color = color[index_letter:]
    stop = color.find(",")
    print(stop)
    final_color = color[:stop]
    print(final_color)







