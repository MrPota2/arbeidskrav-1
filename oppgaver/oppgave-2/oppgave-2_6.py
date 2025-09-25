original_list = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

name_list = original_list[::2]
age_list = original_list[1::2]

dict_list = []

for person in range(len(name_list)):
    person_dict = {
        "navn": name_list[person],
        "alder": age_list[person]
    }
    dict_list.append(person_dict)

print(dict_list)