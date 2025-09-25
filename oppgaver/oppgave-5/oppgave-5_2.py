import csv

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

            # Counter logic
            books_per_genre_dict[row["Sjanger"]] = books_per_genre_dict.get(row["Sjanger"], 0) + 1 # Returns count of genre if exists, otherwise initializes at zero

    # Error summary
    if not verbose and num_of_error_rows > 0:
        print(f"WARNING: {num_of_error_rows} invalid lines skipped.\nFor further details, run function with argument 'True'.")
    if num_of_error_rows > 0: # Adds a seperator line between warnings and output
        print(("=" * 30) + "\n")

    for genre, amount in books_per_genre_dict.items():
        print(f"{genre}: {amount}")

    return books_per_genre_dict

result = books_per_genre()