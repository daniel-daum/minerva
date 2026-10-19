class Algorithm:
    def __init__(self):
        self.numbers = []

        with open("numbers.txt", "r") as file:
            for line in file:
                self.numbers.append(int(line.strip()))

    def output_all_values(self):

        for i in range(len(self.numbers)):
            print(self.numbers[i])

    def output_sum_all_values(self):
        sum = 0

        for i in range(len(self.numbers)):
            sum = sum + self.numbers[i]

        print(sum)

    def output_all_odd(self):

        for i in range(len(self.numbers)):
            if self.numbers[i] % 2 != 0:
                print(self.numbers[i])

    def output_all_even(self):
        for i in range(len(self.numbers)):
            if self.numbers[i] % 2 == 0:
                print(self.numbers[i])

    def linear_search(self, num):
        position = -1

        for i in range(len(self.numbers)):
            if num == self.numbers[i]:
                position = i

        if position != -1:
            print("Number found in array at position " + str(position))
        else:
            print("Number not found in array.")

    def output_middle_value(self):
        print(self.numbers[len(self.numbers) // 2])

    def output_first_value(self):
        print("first value in array: " + str(self.numbers[0]))

    def output_last_value(self):
        print("last value in array: " + str(self.numbers[len(self.numbers) - 1]))

    def output_highest_value_loc(self):
        highest_val = 0
        location = 0

        for i in range(len(self.numbers)):
            if self.numbers[i] > highest_val:
                highest_val = self.numbers[i]
                location = i

        print("highest value: " + str(highest_val) + " , location: " + str(location))

    def output_lowest_value_loc(self):
        lowest_val = 1000
        location = 0

        for i in range(len(self.numbers)):
            if self.numbers[i] < lowest_val:
                lowest_val = self.numbers[i]
                location = i

        print("lowest value: " + str(lowest_val) + " , location: " + str(location))

    def bubble_sort(self):

        for i in range(len(self.numbers) - 1):
            for j in range(len(self.numbers) - 1 - i):
                hold = 0

                if self.numbers[j] < self.numbers[j + 1]:
                    hold = self.numbers[j]
                    self.numbers[j] = self.numbers[j + 1]
                    self.numbers[j + 1] = hold

        for i in range(len(self.numbers)):
            print(self.numbers[i])

    def mean_average(self):
        sum = 0
        average = 0

        for i in range(len(self.numbers)):
            sum = sum + self.numbers[i]

        average = sum / len(self.numbers)

        print("mean_average: " + str(average))


def main():

    task6 = Algorithm()

    task6.output_all_values()
    task6.output_sum_all_values()
    task6.output_all_odd()
    task6.output_all_even()
    task6.linear_search(379)
    task6.output_middle_value()
    task6.output_first_value()
    task6.output_last_value()
    task6.output_highest_value_loc()
    task6.output_lowest_value_loc()
    task6.bubble_sort()
    task6.mean_average()


if __name__ == "__main__":
    main()
