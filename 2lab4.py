import random

a = ['красный', 'желтый', 'синий']

color1 = random.choice(a)
color2 = random.choice(a)

if color1 and color2:
    if color1 != color2:
        if (color1 in ('красный','синий')) and (color2 in ('красный','синий')):
            print(color1,color2)
            print('фиолетовый')
        if (color1 in ('красный','желтый')) and (color2 in ('красный','желтый')):
            print('оранжевый')
            print(color1, color2)
        if (color1 in ('синий', 'желтый')) and (color2 in ('синий', 'желтый')):
            print('зеленый')
            print(color1, color2)







