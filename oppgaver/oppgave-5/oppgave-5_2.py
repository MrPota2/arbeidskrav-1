import csv

from helpers.error_utils import print_error_summary, is_row_columns_valid

def books_per_genre(verbose: bool=False) -> dict:
    """
    Opens and reads *bokutlån.csv*, and sorts each genre into enumerated dictionary entries.

    Has error handling that checks for corrupted rows (empty columns or invalid types).
    :param verbose: Enables verbose error logging.
    :return: Key-value dictionary (key=genre, val=number of books in genre)
    """
    books_per_genre_dict = {}
    num_of_error_rows = 0

    with (open("bokutlån.csv", "r", encoding='utf-8') as csv_file):
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames

        for row_num, row in enumerate(csv_reader, start=1):
            if not is_row_columns_valid(row, row_num, headers, verbose):
                num_of_error_rows += 1
                continue

            # Counter logic
            books_per_genre_dict[row["Sjanger"]] = books_per_genre_dict.get(row["Sjanger"], 0) + 1 # Returns count of genre if exists, otherwise initializes at zero

    # Error summary
    if not verbose and num_of_error_rows > 0:
        print_error_summary(num_of_error_rows)

    for genre, amount in books_per_genre_dict.items():
        print(f"{genre}: {amount}")

    return books_per_genre_dict

result = books_per_genre()