import csv

from helpers.error_utils import print_error_summary, is_row_columns_valid

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
            if not is_row_columns_valid(row, row_num, headers, verbose):
                num_of_error_rows += 1
                continue

            # Extension summarizer:
            extensions += int(row["Forlenget"])

        # Error summary
        if not verbose and num_of_error_rows > 0:
            print_error_summary(num_of_error_rows)

    print(f"Total extension days: {extensions}.")

    return extensions

total_extended_days = get_total_extension_days()