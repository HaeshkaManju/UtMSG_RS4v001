# Make a Hero
import pyinputplus as pyip

hero_data = {
    "Name": "",
    "Spells": [],
    "Skills": []}

spells = ("Might", "Fervor", "Stalwart" , "Ward", "Celerity", "Forced March",
         "Armament", "Midas Touch", "Cornucopia", "Seer", "Druid Lore",
         "Silver-Tongue", "True-Cause", "Napoleon", "Shroud", "Telescoping",
         "Runesmith", "Mind Leech", "Force Cage", "Earth Golem")

leader_combat_skills = ["leadership", "tactics"]

hero_name = pyip.inputStr("What is your Hero's name? ", blank=False)

hero_spells=[]
print("What spells does {} know?".format(hero_name))
choice = 1
while choice != '':
    choice = pyip.inputMenu(spells, numbered=True, blank=True)
    if choice == '':
        break
    else:
        hero_spells.append(choice)

hero_skills={}
print("Which skills does {} know?".format(hero_name))
choice = 1
while choice !='':
    choice = pyip.inputMenu(leader_combat_skills, numbered=True, blank=True)
    if choice == '':
        break
    else:
        num_of_ranks = pyip.inputInt(prompt = "How many ranks in the {} skill? ".format(choice), blank=False)
        hero_skills.update({choice: num_of_ranks})

print(hero_name)
print(hero_spells)
print(hero_skills)

hero_data.update({"Name": hero_name})
hero_data.update({"Spells": hero_spells})
hero_data.update({"Skills": hero_skills})
print(hero_data)