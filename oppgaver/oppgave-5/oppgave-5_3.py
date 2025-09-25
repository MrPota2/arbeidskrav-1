import csv

def average_loan_period(verbose: bool=False) -> float:
    num_of_error_rows = 0

    with (open("bokutlån.csv", "r", encoding='utf-8') as csv_file):
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames

        length_of_loan = []

        for row_num, row in enumerate(csv_reader, start=1):
            # Empty field sanitizer
            if any(row[col] is None or row[col] == "" for col in headers): # Worked with GPT for this line, to find a comparator that would match if ANY column returned None or blank
                num_of_error_rows += 1
                if verbose:
                    print(f"WARNING: Row {row_num} skipped. Empty column detected.")
                continue
            # Value checker for integer-only columns
            try:
                int(row["Forlenget"])
                int(row["Låneperiode"])
            except ValueError as e:
                num_of_error_rows += 1
                if verbose:
                    print(f"WARNING: Row {row_num} skipped. Non-int value in int column: ({e})")
                continue

            total_loan_length = int(row["Forlenget"]) + int(row["Låneperiode"])
            length_of_loan.append(total_loan_length)

        average_loan_length = sum(length_of_loan) / len(length_of_loan)

     # Error summary
    if not verbose and num_of_error_rows > 0:
        print(f"WARNING: {num_of_error_rows} invalid lines skipped.\nFor further details, run function with argument 'True'.")
    if num_of_error_rows > 0: # Adds a seperator line between warnings and output
        print(("=" * 30) + "\n")

    print(f"The average loan length is {average_loan_length:.0f} days.")

    return average_loan_length

result = average_loan_period()
