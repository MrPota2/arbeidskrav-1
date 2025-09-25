def date_checker(date_list: list[int]) -> bool:
    """
    Simplified date value checker, manually validating date and month.
    :param date_list: A split segment of a date
    :return: Returns a bool value, where True = valid date
    """

    if not (1 <= date_list[0] <= 31 and 1 <= date_list[1] <= 12):
        raise ValueError("ERROR: Invalid date format, ensure (dd/mm/yyyy)")

def time_difference_calculator(first_list: list[int], second_list: list[int]) -> int:
    """
    Takes two user-inputted dates (dd/mm/yyyy format) and returns the absolute difference between the two dates.
    :param first_list: A list of date segments
    :param second_list: A list of date segments
    :return: Returns the amount of days between the two selected dates.
    """
    time_difference = 0

    time_difference += first_list[0] - second_list[0] # Day
    time_difference += (first_list[1] - second_list[1]) * 30 # Month
    time_difference += (first_list[2] - second_list[2]) * 365 # Year

    return abs(time_difference) # Drops the sign in case of negative number


first_date = input("Skriv inn den første datoen\n(dd/mm/yyyy): ")
second_date = input("Skriv inn den andre datoen\n(dd/mm/yyyy): ")

first_date_list = [int(segment) for segment in first_date.split("/")]
second_date_list = [int(segment) for segment in second_date.split("/")]

try:
    date_checker(first_date_list)
    date_checker(second_date_list)
except ValueError as e:
    print("Wrong date format: ", e)

else:
    day_difference = time_difference_calculator(first_date_list, second_date_list)
    print(f"{day_difference} dager")

# TODO: Include a datetime version for accuracy?
