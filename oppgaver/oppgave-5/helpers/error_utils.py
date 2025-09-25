
def print_error_summary(error_row_count: int) -> None:
    print(("=" * 30))
    print(f"WARNING: {error_row_count} invalid lines skipped.\nFor further details, run function with argument 'True'.")

    if error_row_count > 0:
        print(("=" * 30) + "\n") # Adds a seperator line between warnings and output


def is_row_columns_valid(row: dict, row_num: int, headers, verbose: bool=False) -> bool:
    """Function returns False if row columns are not valid, and True if there are no errors"""

    # Empty field sanitizer
    if any(row[col] is None or row[col] == "" for col in headers):  # Worked with GPT for this line, to find a comparator that would match if ANY column returned None or blank TODO: add this comment in readme instead
        if verbose:
            print(f"WARNING: Row {row_num} skipped. Empty column detected.")
        return False

    # Value checker for integer-only columns
    try:
        int(row["Forlenget"])
        int(row["Låneperiode"])
    except ValueError as e:
        if verbose:
            print(f"WARNING: Row {row_num} skipped. Non-int value in int column: ({e})")
        return False

    return True