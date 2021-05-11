from pathlib import Path
from collections import OrderedDict


def function(path, file_extension=".txt"):
    directory = Path(path)
    list_of_files = OrderedDict()
    # list_of_files = {}
    for file in directory.glob("**/*" + file_extension):
        # with file.open() as f:
        with open(file) as f:
            list_of_files[f.name] = sum(1 for line in f)

    for key, value in list_of_files.items():
        print(key, value)

    total_number_of_lines = sum(list_of_files.values())
    number_of_files = len(list_of_files)

    print("Number of files found: ", number_of_files)
    print("Total number of lines: ", total_number_of_lines)
    if number_of_files != 0:
        print("Average lines per file: ", total_number_of_lines / number_of_files)
    else:
        print("file is empty")




# function(path=input("Please provide path: "),
#          file_extension=input("Please provide filename extension (example: '.txt'): "))

function(path=input("Please provide path: "), file_extension='.sh')
