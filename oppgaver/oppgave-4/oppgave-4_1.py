import random
import string
from pathlib import Path


def random_filename_generator(file_count: int) -> None:
    """
    Generates *n* files with random file names and extensions from *file_extensions*.
    Places them in */assets/*. If this file path does not exist, the function will create it.
    :param file_count: Number of files to be created
    :return: None
    """
    char_pool = string.ascii_letters + string.digits
    file_extensions = ["txt", "csv", "log"]
    file_path = Path() / "assets"
    file_path.mkdir(parents=True, exist_ok=True)
    files_created = 0

    filename = ''
    while files_created < file_count:
        for char in range(10):
            filename += random.choice(char_pool)
        extension = random.choice(file_extensions)
        with open(f'assets/{filename}.{extension}', 'w') as wf:
            wf.write(f"Dette er fil nummer: {files_created + 1}!")

        files_created += 1
        filename = ''

random_filename_generator(30)
#%% md
## Oppgave 4.2
##### Based on knowledge from: https://www.youtube.com/watch?v=yxa-DJuuTBI