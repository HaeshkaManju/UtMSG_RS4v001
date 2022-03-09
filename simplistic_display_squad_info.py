# test parameters
s_name = "Squaddies"
s_level = 0
s_off = 1
s_def = 1
s_str = 1
spd_ovl = 2
spd_cmb = "M"
rce = "Hum"
m_tools = 2
m_wpn = 2
cost = 10
upkeep = 5
r_bonus = "Adaptive"
skills = {"Mason": 3, "Parry": 2}
# purely hypothetical. 

print("###################################")
print("# Name: {} - Level: {} #".format(s_name, s_level))

print("###################################")
print("# Off  : {}   # Def: {}   # Str: {} #".format(s_off, s_def, s_str))
print("# Spd  : {}{}  # Rce: {} # M_Tools: {} #".format(spd_ovl, spd_cmb, rce, m_tools))
print("# M_Wpn: {}   # Cost: {} # Upk: {} #".format(m_wpn, cost, upkeep))

print("###################################")
print("# Racial Bonus: {} #".format(r_bonus))
for k in skills:
    print("# Skills: {}: {} #".format(k, skills[k]))
print("###################################")  