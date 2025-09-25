selected_number = input("Please enter a positive integer: ")

try:
    int_value = int(selected_number)
except (ValueError, TypeError):
    raise TypeError("The selected number is not an integer")

if int_value <= 0:
    raise ValueError("The selected number must be positive.")

sum_of_number_range = int_value # Starts at selected_number to include the last number as task asks

print(f"Number {int_value} selected.")

for i in range(int_value):
    sum_of_number_range += i

print(f"The sum of all numbers between 0 and {int_value} is:  {sum_of_number_range}.")