import pyinputplus as pyip
num_of_heroes = pyip.inputInt(prompt="How many heroes? ", blank=True)
global hero_info
hero_info = []
for x in range(1, num_of_heroes+1):
    hero_info.append("hero{}".format(int(x)))
    
print(hero_info)