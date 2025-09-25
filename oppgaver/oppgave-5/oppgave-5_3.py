import csv

from helpers.error_utils import print_error_summary, is_row_columns_valid

def average_loan_period(verbose: bool=False) -> float:
    num_of_error_rows = 0

    with (open("bokutlån.csv", "r", encoding='utf-8') as csv_file):
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames

        length_of_loan = []

        for row_num, row in enumerate(csv_reader, start=1):
            if not is_row_columns_valid(row, row_num, headers, verbose):
                num_of_error_rows += 1
                continue

            total_loan_length = int(row["Forlenget"]) + int(row["Låneperiode"])
            length_of_loan.append(total_loan_length)

        average_loan_length = sum(length_of_loan) / len(length_of_loan)

     # Error summary
    if not verbose and num_of_error_rows > 0:
        print_error_summary(num_of_error_rows)

    print(f"The average loan length is {average_loan_length:.0f} days.")

    return average_loan_length

result = average_loan_period()
