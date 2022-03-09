import pyinputplus as pyip

leader_combat_skills = ["leadership", "tactics"]

def which_chief_skills(chief_skills_known):
    print("Which skills does your Chief know?")
    choice = 1
    while choice !='':
        choice = pyip.inputMenu(leader_combat_skills, numbered=True, blank=True)
        if choice == '':
            break
        else:
            num_of_ranks = pyip.inputInt(prompt = "How many ranks in the skill? ", blank=False)
            chief_skills_known.update({choice: num_of_ranks})
    return chief_skills_known

def which_cohort_skills(cohort_skills_known):
    print("Which skills does your Cohort know?")
    choice = 1
    while choice !='':
        choice = pyip.inputMenu(leader_combat_skills, numbered=True, blank=True)
        if choice == '':
            break
        else:
            num_of_ranks = pyip.inputInt(prompt = "How many ranks in the skill? ", blank=False)
            cohort_skills_known.update({choice: num_of_ranks})
    return cohort_skills_known

chief_skills_known={}
which_chief_skills(chief_skills_known)
print(chief_skills_known)
cohort_skills_known={}
which_cohort_skills(chief_skills_known)
print(cohort_skills_known)
