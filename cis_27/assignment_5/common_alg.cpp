#include "common_alg.h"

#include <fstream>
#include <iostream>

// constructor:  fill array from numbers.txt
Common_Alg::Common_Alg() {
  size = 1000;
  numbers = new int[size]();

  int i = 0;
  std::ifstream file("numbers.txt");

  if (file.is_open()) {
    int num;

    while (i < size && file >> num) {
      numbers[i] = num;
      i++;
    }
    file.close();
  } else {
    std::cout << "could not open numbers.txt\n";
  }
}

// destructor: free the memory made with new
Common_Alg::~Common_Alg() {
  delete[] numbers;
  numbers = nullptr;
  std::cout << "destructor: dynamic array freed\n";
}

// method 1: output all values
void Common_Alg::output_all_values() {

  for (int i = 0; i < size; i++) {
    std::cout << numbers[i] << "\n";
  }
}

// method 2: output sum of all values
void Common_Alg::output_sum_all_values() {
  int sum = 0;

  for (int i = 0; i < size; i++) {
    sum = sum + numbers[i];
  }
  std::cout << sum << "\n";
}

// method 3: output all odd numbers
void Common_Alg::output_all_odd() {

  for (int i = 0; i < size; i++) {
    if (numbers[i] % 2 != 0) {
      std::cout << numbers[i] << "\n";
    }
  }
}

// method 4: output all even numbers
void Common_Alg::output_all_even() {
  for (int i = 0; i < size; i++) {
    if (numbers[i] % 2 == 0) {
      std::cout << numbers[i] << "\n";
    }
  }
}

// method 5: binary search for a value
void Common_Alg::binary_search(int num) {
    
  // data must be in sorted first
  bubble_sort();

  int low = 0;
  int high = size - 1;
  int position = -1;

  while (low <= high) {
    int mid = (low + high) / 2;

    if (numbers[mid] == num) {
      position = mid;
      break;
    } else if (numbers[mid] > num) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  if (position != -1) {
    std::cout << "Number found in array at position " << position << "\n";
  } else {
    std::cout << "Number not found in array.\n";
  }
}

// method 6: output middle value
void Common_Alg::output_middle_value() {
  std::cout << numbers[size / 2] << "\n";
}

// method 7: output first value in the array
void Common_Alg::output_first_value() {
  std::cout << "first value in array: " << numbers[0] << "\n";
}

// method 8: output last value in the array
void Common_Alg::output_last_value() {
  std::cout << "last value in array: " << numbers[size - 1] << "\n";
}

// method 9: output highest value, and its location in the array
void Common_Alg::output_highest_value_loc() {
  int highest_val = 0;
  int location = 0;

  for (int i = 0; i < size; i++) {
    if (numbers[i] > highest_val) {
      highest_val = numbers[i];
      location = i;
    }
  }
  std::cout << "highest value: " << highest_val << " , location: " << location
            << "\n";
}

// method 10: output lowest value and its location in the array
void Common_Alg::output_lowest_value_loc() {
  int lowest_val = 1000;
  int location = 0;

  for (int i = 0; i < size; i++) {
    if (numbers[i] < lowest_val) {
      lowest_val = numbers[i];
      location = i;
    }
  }
  std::cout << "lowest value: " << lowest_val << " , location: " << location
            << "\n";
}

// bubble sort, largest to smallest (used by method 5 and method 11)
void Common_Alg::bubble_sort() {

  for (int i = 0; i < size - 1; i++) {

    for (int j = 0; j < size - 1 - i; j++) {
      int hold = 0;

      if (numbers[j] < numbers[j + 1]) {
        hold = numbers[j];
        numbers[j] = numbers[j + 1];
        numbers[j + 1] = hold;
      }
    }
  }
}

// method 11: bubble sort, then output the sorted values
void Common_Alg::output_bubble_sort() {
  bubble_sort();

  for (int i = 0; i < size; i++) {
    std::cout << numbers[i] << "\n";
  }
}

// method 12: output mean average
void Common_Alg::mean_average() {
  int sum = 0;
  int average = 0;

  for (int i = 0; i < size; i++) {
    sum = sum + numbers[i];
  }

  average = sum / size;

  std::cout << "mean_average: " << average << "\n";
}
