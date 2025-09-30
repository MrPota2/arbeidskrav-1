from datetime import date, timedelta

def get_validated_date() -> date | bool:
    date_list = input("Skriv inn dato\n(dd/mm/yyyy): ").split("/")

    try:
        date_list = [int(segment) for segment in date_list]
    except ValueError as e:
        print(f"Error: non-integer value in date segment: {e}")
        return False

    try:
        date_object = date(date_list[2], date_list[1], date_list[0])
    except ValueError as e:
        print(f"Error: Value entered is not a valid date: {e}")
        return False
    else:
        return date_object


def time_difference_calculator(first_date_obj: date, second_date_obj: date) -> int:
    difference_in_days = abs((first_date_obj - second_date_obj).days)
    return difference_in_days


first_date = get_validated_date()
second_date = get_validated_date()

print(
    "Det er "
    f"{time_difference_calculator(first_date, second_date)} "
    f"dager mellom {first_date.strftime("%d.%m.%y")} og {second_date.strftime("%d.%m.%y")}."
)