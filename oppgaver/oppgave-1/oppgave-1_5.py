base_number = int(input("Please enter the starting of the range: "))
top_number = int(input("Now, please enter the top number of the range: "))

padding_len = 4

print("| ", end="") # Used ChatGPT for tips resulting in the end=""
for number in range(base_number, top_number):
    print(f"{str(number).center(padding_len)} | ", end="")

print("\n|", end="")

for number in range(base_number, top_number):
    print("-" + "-" * padding_len + "-|", end="")

print()
for multiple in range(1, 11):
    for multiple_index in range(base_number, top_number):
        print(f"| {str(multiple_index * multiple).center(padding_len)} ", end="")
    print("|")
