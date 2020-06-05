def user(first_name, last_name, **informations):
    profile = {}
    profile["first_name"] = first_name
    profile["last_name"] = last_name

    for k, v in informations.items():
        profile[k] = v

    return profile

def print_profile(profile):
    for k,v in profile.items():
        print(k, ":", v)

profilex = user("david", "potvin", eye_color="blue", hair_color="red")
print_profile(profilex)
