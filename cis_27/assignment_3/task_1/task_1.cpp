#include <cstdlib>
#include <ctime>
#include <iostream>

const int SIZE = 1000;

class Common_Alg {
private:
  int numbers[SIZE];

public:
  // constructor: seed rand, fill array with 1000 random ints from 1 to 1000
  Common_Alg() {
    srand(time(0));

    for (int i = 0; i < SIZE; i++) {
      numbers[i] = rand() % 1000 + 1;
    }
  }

  // method 1: output all values
  void output_all_values() {

    for (int i = 0; i < SIZE; i++) {
      std::cout << numbers[i] << "\n";
    }
  }

  // method 2: output sum of all values
  void output_sum_all_values() {
    int sum = 0;

    for (int i = 0; i < SIZE; i++) {
      sum = sum + numbers[i];
    }
    std::cout << sum << "\n";
  }

  // method 3: output all odd numbers
  void output_all_odd() {

    for (int i = 0; i < SIZE; i++) {
      if (numbers[i] % 2 != 0) {
        std::cout << numbers[i] << "\n";
      }
    }
  }

  // method 4: output all even numbers
  void output_all_even() {
    for (int i = 0; i < SIZE; i++) {
      if (numbers[i] % 2 == 0) {
        std::cout << numbers[i] << "\n";
      }
    }
  }

  // method 5: linear search, output every position the value is found at
  void linear_search(int num) {
    bool found = false;

    for (int i = 0; i < SIZE; i++) {
      if (num == numbers[i]) {
        std::cout << "Number found in array at position " << i << "\n";
        found = true;
      }
    }

    if (!found) {
      std::cout << "Number not found in array.\n";
    }
  }

  // method 6: output the two middle values (location 499 and 500)
  void output_middle_values() {
    std::cout << "middle value at location " << SIZE / 2 - 1 << ": "
              << numbers[SIZE / 2 - 1] << "\n";
    std::cout << "middle value at location " << SIZE / 2 << ": "
              << numbers[SIZE / 2] << "\n";
  }

  // method 7: output first value in the array
  void output_first_value() {
    std::cout << "first value in array: " << numbers[0] << "\n";
  }

  // method 8: output last value in the array
  void output_last_value() {
    std::cout << "last value in array: " << numbers[SIZE - 1] << "\n";
  }

  // method 9: output highest value, and its location in the array
  void output_highest_value_loc() {
    int highest_val = 0;
    int location = 0;

    for (int i = 0; i < SIZE; i++) {
      if (numbers[i] > highest_val) {
        highest_val = numbers[i];
        location = i;
      }
    }
    std::cout << "highest value: " << highest_val << " , location: " << location
              << "\n";
  }

  // method 10: output lowest value and its location in the array
  void output_lowest_value_loc() {
    int lowest_val = 1000;
    int location = 0;

    for (int i = 0; i < SIZE; i++) {
      if (numbers[i] < lowest_val) {
        lowest_val = numbers[i];
        location = i;
      }
    }
    std::cout << "lowest value: " << lowest_val << " , location: " << location
              << "\n";
  }

  // bubble sort, largest to smallest (used by method 11 and method 13)
  void bubble_sort(int arr[]) {

    for (int i = 0; i < SIZE - 1; i++) {

      for (int j = 0; j < SIZE - 1 - i; j++) {
        int hold = 0;

        if (arr[j] < arr[j + 1]) {
          hold = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = hold;
        }
      }
    }
  }

  // method 11: bubble sort the array, then output the sorted values
  void output_bubble_sort() {
    bubble_sort(numbers);

    for (int i = 0; i < SIZE; i++) {
      std::cout << numbers[i] << "\n";
    }
  }

  // method 12: output mean average as a decimal
  void mean_average() {
    int sum = 0;
    double average = 0;

    for (int i = 0; i < SIZE; i++) {
      sum = sum + numbers[i];
    }

    average = (double)sum / SIZE;

    std::cout << "mean_average: " << average << "\n";
  }

  // method 13: median, sort a copy and average the two middle values
  void median() {
    int copy[SIZE];

    for (int i = 0; i < SIZE; i++) {
      copy[i] = numbers[i];
    }
    bubble_sort(copy);

    double median_val = (copy[SIZE / 2 - 1] + copy[SIZE / 2]) / 2.0;

    std::cout << "median: " << median_val << "\n";
  }
};

int main() {

  Common_Alg task1;
  int choice = -1;

  while (choice != 0) {
    std::cout << "\n----- menu -----\n";
    std::cout << "1. output all values\n";
    std::cout << "2. output sum of all values\n";
    std::cout << "3. output all odd numbers\n";
    std::cout << "4. output all even numbers\n";
    std::cout << "5. linear search\n";
    std::cout << "6. output middle values\n";
    std::cout << "7. output first value\n";
    std::cout << "8. output last value\n";
    std::cout << "9. output highest value and location\n";
    std::cout << "10. output lowest value and location\n";
    std::cout << "11. bubble sort\n";
    std::cout << "12. output mean average\n";
    std::cout << "13. output median\n";
    std::cout << "0. exit\n";
    std::cout << "choice: ";

    // not a number: clear the error and throw away the bad input
    if (!(std::cin >> choice)) {
      if (std::cin.eof()) {
        break;
      }
      std::cin.clear();
      std::cin.ignore(10000, '\n');
      std::cout << "invalid choice, enter a number\n";
      choice = -1;
      continue;
    }

    // remove the leftover newline
    std::cin.ignore(10000, '\n');

    switch (choice) {
    case 1:
      task1.output_all_values();
      break;
    case 2:
      task1.output_sum_all_values();
      break;
    case 3:
      task1.output_all_odd();
      break;
    case 4:
      task1.output_all_even();
      break;
    case 5: {
      int num;
      std::cout << "enter a search value: ";

      if (!(std::cin >> num)) {
        std::cin.clear();
        std::cin.ignore(10000, '\n');
        std::cout << "invalid value, enter a number\n";
        break;
      }
      std::cin.ignore(10000, '\n');
      task1.linear_search(num);
      break;
    }
    case 6:
      task1.output_middle_values();
      break;
    case 7:
      task1.output_first_value();
      break;
    case 8:
      task1.output_last_value();
      break;
    case 9:
      task1.output_highest_value_loc();
      break;
    case 10:
      task1.output_lowest_value_loc();
      break;
    case 11:
      task1.output_bubble_sort();
      break;
    case 12:
      task1.mean_average();
      break;
    case 13:
      task1.median();
      break;
    case 0:
      break;
    default:
      std::cout << "invalid choice\n";
    }
  }

  return 0;
}

// g++ -std=c++17 -Wall -o task1 task_1.cpp
