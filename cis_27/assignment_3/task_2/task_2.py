import random


class Common_Alg:
    # constructor: fill the list with 1000 random ints from 1 to 1000
    def __init__(self):
        self.numbers = []

        for i in range(1000):
            self.numbers.append(random.randint(1, 1000))

    # method 1: output all values
    def output_all_values(self):

        for i in range(len(self.numbers)):
            print(self.numbers[i])

    # method 2: output sum of all values
    def output_sum_all_values(self):
        sum = 0

        for i in range(len(self.numbers)):
            sum = sum + self.numbers[i]

        print(sum)

    # method 3: output all odd numbers
    def output_all_odd(self):

        for i in range(len(self.numbers)):
            if self.numbers[i] % 2 != 0:
                print(self.numbers[i])

    # method 4: output all even numbers
    def output_all_even(self):
        for i in range(len(self.numbers)):
            if self.numbers[i] % 2 == 0:
                print(self.numbers[i])

    # method 5: linear search, output every position the value is found at
    def linear_search(self, num):
        found = False

        for i in range(len(self.numbers)):
            if num == self.numbers[i]:
                print("Number found in array at position " + str(i))
                found = True

        if not found:
            print("Number not found in array.")

    # method 6: output the two middle values (location 499 and 500)
    def output_middle_values(self):
        middle = len(self.numbers) // 2

        print("middle value at location " + str(middle - 1) + ": " + str(self.numbers[middle - 1]))
        print("middle value at location " + str(middle) + ": " + str(self.numbers[middle]))

    # method 7: output first value in the array
    def output_first_value(self):
        print("first value in array: " + str(self.numbers[0]))

    # method 8: output last value in the array
    def output_last_value(self):
        print("last value in array: " + str(self.numbers[len(self.numbers) - 1]))

    # method 9: output highest value, and its location in the array
    def output_highest_value_loc(self):
        highest_val = 0
        location = 0

        for i in range(len(self.numbers)):
            if self.numbers[i] > highest_val:
                highest_val = self.numbers[i]
                location = i

        print("highest value: " + str(highest_val) + " , location: " + str(location))

    # method 10: output lowest value and its location in the array
    def output_lowest_value_loc(self):
        lowest_val = 1000
        location = 0

        for i in range(len(self.numbers)):
            if self.numbers[i] < lowest_val:
                lowest_val = self.numbers[i]
                location = i

        print("lowest value: " + str(lowest_val) + " , location: " + str(location))

    # bubble sort, largest to smallest (used by method 11 and method 13)
    def bubble_sort(self, arr):

        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                hold = 0

                if arr[j] < arr[j + 1]:
                    hold = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = hold

    # method 11: bubble sort the list, then output the sorted values
    def output_bubble_sort(self):
        self.bubble_sort(self.numbers)

        for i in range(len(self.numbers)):
            print(self.numbers[i])

    # method 12: output mean average as a decimal
    def mean_average(self):
        sum = 0
        average = 0

        for i in range(len(self.numbers)):
            sum = sum + self.numbers[i]

        average = sum / len(self.numbers)

        print("mean_average: " + str(average))

    # method 13: median, sort a copy and average the two middle values
    def median(self):
        copy = []

        for i in range(len(self.numbers)):
            copy.append(self.numbers[i])

        self.bubble_sort(copy)

        middle = len(copy) // 2
        median_val = (copy[middle - 1] + copy[middle]) / 2

        print("median: " + str(median_val))


def main():

    task2 = Common_Alg()
    choice = -1

    while choice != 0:
        print("\n----- menu -----")
        print("1. output all values")
        print("2. output sum of all values")
        print("3. output all odd numbers")
        print("4. output all even numbers")
        print("5. linear search")
        print("6. output middle values")
        print("7. output first value")
        print("8. output last value")
        print("9. output highest value and location")
        print("10. output lowest value and location")
        print("11. bubble sort")
        print("12. output mean average")
        print("13. output median")
        print("0. exit")

        # not a number: ask again
        try:
            choice = int(input("choice: "))
        except ValueError:
            print("invalid choice, enter a number")
            continue

        if choice == 1:
            task2.output_all_values()
        elif choice == 2:
            task2.output_sum_all_values()
        elif choice == 3:
            task2.output_all_odd()
        elif choice == 4:
            task2.output_all_even()
        elif choice == 5:
            try:
                num = int(input("enter a search value: "))
            except ValueError:
                print("invalid value, enter a number")
                continue
            task2.linear_search(num)
        elif choice == 6:
            task2.output_middle_values()
        elif choice == 7:
            task2.output_first_value()
        elif choice == 8:
            task2.output_last_value()
        elif choice == 9:
            task2.output_highest_value_loc()
        elif choice == 10:
            task2.output_lowest_value_loc()
        elif choice == 11:
            task2.output_bubble_sort()
        elif choice == 12:
            task2.mean_average()
        elif choice == 13:
            task2.median()
        elif choice != 0:
            print("invalid choice")


if __name__ == "__main__":
    main()
