
print("################################################")
print("Section 1 - Super Basic.")
warehouse = [ "some stuff" ]
mySquad = [ "this stuff" ]

print("Your Squad currently has the following equipped:")
for item in mySquad:
	print(item)

print("Your warehouse has the following in storage: ")
for stored in warehouse:
    print(stored)

if "some stuff" in warehouse:
    warehouse.remove("some stuff")
    mySquad.append("some stuff")

print("Your Squad currently now has the following equipped: ")
for item in mySquad:
    print(item)
print("################################################")

##################################################################################

print("################################################")
print("Section 2 - Moving Stuff with Functions for clarity.")

warehouse1 = ["Weapons"]
mySquad1 = ["Shields"]

def what_items_present(target, loc):
	print("Your {} has the following item(s):".format(loc))
    for item in target:
        print(item)

what_items_present(warehouse1, loc="Warehouse")
what_items_present(mySquad, loc="Squad")
print("Let's move the Weapons from the Warehouse onto your Squad.")
def attempt_To_Equip_Weapons(fromTarget, toTarget):
    if "Weapons"

print("################################################")