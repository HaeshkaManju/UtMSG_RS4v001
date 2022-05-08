# assign the names, merge the names.
import pyinputplus as pyip

def assign_name(ltype):
    x = pyip.inputStr("{} name? ".format(ltype))
    if ltype == 'chief':
        tempname = {'chief name': x}
    else:
        tempname = {'cohort name': x}
    return tempname

chief_name = assign_name('chief')
# print(chief_name)
cohort_name = assign_name('cohort')
# print(cohort_name)
leader_names = {**chief_name, **cohort_name}
# print(leader_names)

# do some kwargs to this func to take any number of leader names and kick out the appropriate dictionary.
def display_leader_names():
    for k in leader_names:
        print("Your {} is {}".format(k, leader_names[k]))

display_leader_names()
