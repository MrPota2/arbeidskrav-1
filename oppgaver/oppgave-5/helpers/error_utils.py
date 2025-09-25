
def print_error_summary(error_row_count: int) -> None:
    print(("=" * 30))
    print(f"WARNING: {error_row_count} invalid lines skipped.\nFor further details, run function with argument 'True'.")

    if error_row_count > 0:
        print(("=" * 30) + "\n") # Adds a seperator line between warnings and output