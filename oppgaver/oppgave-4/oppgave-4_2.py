from pathlib import Path

def file_sorter() -> None:
    """
    Takes unsorted files from *sorted_path* path, creates the folders specified in *sorting_extensions*
    and sorts the files into each list accordingly.

    If *sorted_path* folders do not exist, the function will add them.
    :return: None
    """
    sorting_extensions = ["txt", "csv", "log"]
    sorted_path = Path() / "assets" / "SortedFiles"

    # Dynamic folder creation
    sorted_path.mkdir(parents=True, exist_ok=True)
    for ext in sorting_extensions:
        subdir_path = sorted_path / ext
        if not Path(ext).exists():
            subdir_path.mkdir(exist_ok=True)

        for file in sorted_path.parent.glob(f"*.{ext}"):
            file.replace(sorted_path / ext / file.name)


file_sorter()