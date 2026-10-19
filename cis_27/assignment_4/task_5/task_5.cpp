// 1. have a main func
// 2. have a class
// 3. declare and fill arary with 1000 rand ints from .txt file, in class
// constructor method 3: output all odd numbers method 4: output all even
// numbers method 5: implement linear search for a value method 6: output middle
// value method 7: output first value in the array method 8: output last value
// in the array method 9: output highest value, and its location in the array
// method 10: output lowest value and its location in the array
// method 11: implement a bubble sort
// method 12: output mean average

#include <fstream>
#include <iostream>

class Algorithms {
public:
  int numbers[1000];

  // constructor
  Algorithms() {
    int i = 0;
    std::ifstream file("numbers.txt");

    if (file.is_open()) {
      int num;

      while (file >> num) {
        numbers[i] = num;
        i++;
      }
      file.close();
    }
  };

  // method 1: output all values
  void output_all_values() {

    for (int i = 0; i < 1000; i++) {
      std::cout << numbers[i] << "\n";
    }
  }

  void output_sum_all_values() {
    int sum = 0;

    for (int i = 0; i < 1000; i++) {
      sum = sum + numbers[i];
    }
    std::cout << sum << "\n";
  }

  // method 3: output all odd numbers
  void output_all_odd() {

    for (int i = 0; i < 1000; i++) {
      if (numbers[i] % 2 != 0) {
        std::cout << numbers[i] << "\n";
      }
    }
  }

  // method 4: output all even numbers
  void output_all_even() {
    for (int i = 0; i < 1000; i++) {
      if (numbers[i] % 2 == 0) {
        std::cout << numbers[i] << "\n";
      }
    }
  }

  // method 5: implement linear search for a value
  void linear_search(int num) {
    int position = -1;

    for (int i = 0; i < 1000; i++) {
      if (num == numbers[i]) {
        position = i;
      }
    }

    if (position != -1) {
      std::cout << "Number found in array at position " << position << "\n";
    } else {
      std::cout << "Number not found in array.";
    }
  }

  // method 6: output middle value
  void output_middle_value() {}
  // method 7: output first value in the array
  void output_first_value() {
    std::cout << "first value in array: " << numbers[0] << "\n";
  }

  // method 8: output last value in the array
  void output_last_value() {
    std::cout << "last value in array: " << numbers[999] << "\n";
  }

  // method 9: output highest value, and its location in the array
  void output_highest_value_loc() {
    int highest_val = 0;
    int location = 0;

    for (int i = 0; i < 1000; i++) {
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

    for (int i = 0; i < 1000; i++) {
      if (numbers[i] < lowest_val) {
        lowest_val = numbers[i];
        location = i;
      }
    }
    std::cout << "lowest value: " << lowest_val << " , location: " << location
              << "\n";
  }
  // method 11: implement a bubble sort
  void bubble_sort() {

    for (int i = 0; i < 999; i++) {

      for (int j = 0; j < 999 - i; j++) {
        int hold = 0;

        if (numbers[j] < numbers[j + 1]) {
          hold = numbers[j];
          numbers[j] = numbers[j + 1];
          numbers[j + 1] = hold;
        }
      }
    }

    for (int i = 0; i < 1000; i++) {
      std::cout << numbers[i] << "\n";
    }
  }

  // method 12: output mean average
  void mean_average() {
    int sum = 0;
    int average = 0;

    for (int i = 0; i < 1000; i++) {
      sum = sum + numbers[i];
    }

    average = sum / 1000;

    std::cout << "mean_average: " << average << "\n";
  }
};

int main() {

  Algorithms task5;

  task5.output_all_values();
  task5.output_sum_all_values();
  task5.output_all_odd();
  task5.output_all_even();
  task5.linear_search(379);
  task5.output_middle_value();
  task5.output_first_value();
  task5.output_last_value();
  task5.output_highest_value_loc();
  task5.output_lowest_value_loc();
  task5.bubble_sort();
  task5.mean_average();

  return 0;
}

// g++ -std=c++17 -o task5 task_5.cpp
