import csv

from helpers.error_utils import print_error_summary

def list_unreturned_books(verbose: bool=False) -> list:
    books_not_returned = []
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

            if row["Tilbakelevert"].strip().lower() == 'nei':
                full_name = f"{row["Fornavn"]} {row["Etternavn"]}"
                books_not_returned.append((row["Boktittel"], full_name))

    # Error summary
        if not verbose and num_of_error_rows > 0:
            print_error_summary(num_of_error_rows)

    return books_not_returned

result = list_unreturned_books()
print(result)