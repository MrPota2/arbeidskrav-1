import datetime

day = int(input("Enter day of month: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

try:
    dato = datetime.date(year, month, day)
except ValueError:
    print("Selected date is invalid.\nPlease try again.")
else:
    print(f"The date '{dato}' is valid! :)")