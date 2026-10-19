# download historyofc++.txt
# read data into a file buffer
# count number of words present in the file (space delimeted)
# output number of words present to the console


def read_file():
    filename = "HistoryofC++.txt"

    with open(filename, "r") as file:
        buffer = file.read().split()

    print(f"There are {len(buffer)} words in the {filename} file.")


read_file()
