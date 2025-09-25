import csv

from helpers.error_utils import print_error_summary

def get_total_extension_days(verbose: bool=False) -> int:
    """
    Opens and reads file, adds extension days together per book to output the total number of extended days

    :param verbose: Enables verbose error logging.
    :return: An integer representing total amount of extended days for all books
    """
    num_of_error_rows = 0
    extensions = 0

    with (open("bokutlån.csv", "r", encoding='utf-8') as csv_file):
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames

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

            # Extension summarizer:
            extensions += int(row["Forlenget"])

        # Error summary
        if not verbose and num_of_error_rows > 0:
            print_error_summary(num_of_error_rows)

    print(f"Total extension days: {extensions}.")

    return extensions

total_extended_days = get_total_extension_days()