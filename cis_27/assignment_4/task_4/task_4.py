numbers = []


with open("numbers.txt", "r") as file:
    for line in file:
        numbers.append(int(line.strip()))

for i in numbers:
    print(i * 10)

# didn't use a while loop in py file cause why. 