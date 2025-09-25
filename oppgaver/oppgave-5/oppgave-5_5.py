import csv

from helpers.error_utils import print_error_summary, is_row_columns_valid

def get_most_borrowed_books(verbose: bool=False) -> dict:
    """

    :param verbose:
    :return:
    """

    borrowed_books = {}
    num_of_error_rows = 0

    with (open("bokutlån.csv", "r", encoding='utf-8') as csv_file):
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames

        for row_num, row in enumerate(csv_reader, start=1):
            if not is_row_columns_valid(row, row_num, headers, verbose):
                num_of_error_rows += 1
                continue

            borrowed_books[row["Boktittel"]] = borrowed_books.get(row["Boktittel"], 0) + 1 # Same logic used in 5.2

    borrowed_books_sorted = {key: value for key, value in sorted(borrowed_books.items(), key=lambda book: (-book[1], book[0]))} # Used Stack Overflow to figure out how to negate only one of the values for correct sorting

    # Error summary
    if not verbose and num_of_error_rows > 0:
        print_error_summary(num_of_error_rows)

    for title, amount in borrowed_books_sorted.items():
        print(f"{title}: {amount}")

    return borrowed_books_sorted

result = get_most_borrowed_books()

