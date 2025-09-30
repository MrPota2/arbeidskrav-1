original_list = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

name_list = original_list[::2]
age_list = original_list[1::2]

person_dict = {}

for person in range(0, len(name_list)):
    person_dict[name_list[person]] = age_list[person]

def dict_sorter_by_name(dict: dict) -> dict:
    """
    Sorts an input dictionary by name in alphabetical order.
    :param dict: Dictionary of ({name: age})
    :return: Returns a dictionary sorted by name. Additionally, prints the values to console
    """
    sorted_dict = {key: value for key, value in sorted(dict.items(), key=lambda entry: entry[0])}

    for name, age in sorted_dict.items():
        print(f"{name} er {age} år.")

    return sorted_dict

sorted_person_dict = dict_sorter_by_name(person_dict)

# vvv 2.5 vvv

sorted_person_list = []

for person, age in sorted_person_dict.items():
    sorted_person_list.append(person)
    sorted_person_list.append(age)

print(sorted_person_list)