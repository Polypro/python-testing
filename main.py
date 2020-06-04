import math
guest_list = ["Rob", "Joe", "Gavin", "Peter", "X", "DMX"]
guest_substitute = ["Caitlyn", "Jenna", "Ford"]
# 0 : guest accepted the invitation
# 1 : guest cannot make it
guest_list_status = [0, 0, 1, 0, 1, 0]
n_absent = sum(guest_list_status)
n_substitute = len(guest_substitute)
absent = 0
for x in range(len(guest_list)):
    if guest_list_status[x] == 0:
        print(guest_list[x], "will come to the party")
    else:
        print(guest_list[x], "cannot make it to the party so", guest_substitute[absent], "will replace this guest")
        guest_list.pop(x)
        guest_list.append(guest_substitute[absent])
        absent+=1

print("\n final list :", guest_list)