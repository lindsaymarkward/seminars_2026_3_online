"""
Write a program to read a file and print ONLY the lines that
start with a #
The user should enter the filename.
"""
file_name = input("What is the file name? ")
try:
    in_file = open(file_name, "r")
    for line in in_file:
        if line.lstrip().startswith("#"):
            print(line.rstrip())
    in_file.close()
except FileNotFoundError:
    print(f"{file_name} not found")
