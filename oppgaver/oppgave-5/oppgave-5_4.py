import csv

from helpers.error_utils import print_error_summary, is_row_columns_valid

def list_unreturned_books(verbose: bool=False) -> list:
    books_not_returned = []
    num_of_error_rows = 0

    with (open("bokutlån.csv", "r", encoding='utf-8') as csv_file):
        csv_reader = csv.DictReader(csv_file)
        headers = csv_reader.fieldnames

        for row_num, row in enumerate(csv_reader, start=1):
            if not is_row_columns_valid(row, row_num, headers, verbose):
                num_of_error_rows += 1
                continue

            if row["Tilbakelevert"].strip().lower() == 'nei':
                full_name = f"{row["Fornavn"]} {row["Etternavn"]}"
                books_not_returned.append((row["Boktittel"], full_name))

    # Error summary
        if not verbose and num_of_error_rows > 0:
            print_error_summary(num_of_error_rows)

    return books_not_returned

result = list_unreturned_books()
print(result)