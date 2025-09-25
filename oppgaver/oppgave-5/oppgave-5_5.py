import csv

from helpers.error_utils import print_error_summary

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

            borrowed_books[row["Boktittel"]] = borrowed_books.get(row["Boktittel"], 0) + 1 # Same logic used in 5.2

    borrowed_books_sorted = {key: value for key, value in sorted(borrowed_books.items(), key=lambda book: (-book[1], book[0]))} # Used Stack Overflow to figure out how to negate only one of the values for correct sorting

    # Error summary
    if not verbose and num_of_error_rows > 0:
        print_error_summary(num_of_error_rows)

    for title, amount in borrowed_books_sorted.items():
        print(f"{title}: {amount}")

    return borrowed_books_sorted

result = get_most_borrowed_books()

