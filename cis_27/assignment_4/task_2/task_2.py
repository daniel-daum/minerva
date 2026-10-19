import random

numbers = []

for i in range(1000):
    rand_num = random.randint(1, 10000)
    numbers.append(rand_num)
    print(rand_num)

with open("numbers.txt", "w") as file:
    for i in numbers:
        file.write(str(i) + "\n")
