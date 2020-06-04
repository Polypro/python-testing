guest_list = ["Rob", "Joe", "Gavin", "Peter"]
# 0 : guest accepted the invitation
# 1 : guest cannot make it
guest_list_status = [0, 0, 1, 0]
for x in range(len(guest_list)):
    if guest_list_status[x] == 0:
        print(guest_list[x],  "will come to the party")
    else:
        print(guest_list[x], "cannot make it to the party")