original_list = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

name_list = original_list[::2]
age_list = original_list[1::2]

# vvv 2.3 vvv

person_dict = {}

for person in range(0, len(name_list)):
    person_dict[name_list[person]] = age_list[person]

for name, age in person_dict.items():
    print(f"{name} er {age} år.")