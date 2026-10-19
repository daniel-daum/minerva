// 1. read float values from floatvalues.txt into a file buffer
// 2. sum all values and output to the console
// 3. output the highest value to the console
// 4. output the lowest value to the console
// 5. append sum and mean average to the end of floatvalues.txt

#include "main.h"

#include <fstream>
#include <iomanip>
#include <iostream>

// constructor: read float values from floatvalues.txt into the array
FloatValues::FloatValues() {
  int i = 0;
  std::ifstream file("floatvalues.txt");

  if (file.is_open()) {
    double value;

    while (file >> value) {
      values[i] = value;
      i++;
    }
    file.close();
  }
}

// method 1: output all values
void FloatValues::output_all_values() {

  for (int i = 0; i < 11; i++) {
    std::cout << values[i] << "\n";
  }
}

// method 2: add up all values in the array
double FloatValues::get_sum() {
  double sum = 0;

  for (int i = 0; i < 11; i++) {
    sum = sum + values[i];
  }
  return sum;
}

// method 3: output sum of all values
void FloatValues::output_sum() { std::cout << "sum: " << get_sum() << "\n"; }

// method 4: output highest value
void FloatValues::output_highest_value() {
  double highest_val = values[0];

  for (int i = 0; i < 11; i++) {
    if (values[i] > highest_val) {
      highest_val = values[i];
    }
  }
  std::cout << "highest value: " << highest_val << "\n";
}

// method 5: output lowest value
void FloatValues::output_lowest_value() {
  double lowest_val = values[0];

  for (int i = 0; i < 11; i++) {
    if (values[i] < lowest_val) {
      lowest_val = values[i];
    }
  }
  std::cout << "lowest value: " << lowest_val << "\n";
}

// method 6: mean average
double FloatValues::get_mean_average() { return get_sum() / 11; }

// method 7: output mean average
void FloatValues::output_mean_average() {
  std::cout << "mean average: " << get_mean_average() << "\n";
}

// method 8: append sum and mean average to the end of floatvalues.txt
void FloatValues::append_results() {
  std::ofstream file("floatvalues.txt", std::ios::app);

  if (file.is_open()) {
    file << std::fixed << std::setprecision(2);
    file << "\nsum: " << get_sum() << "\n";
    file << "mean average: " << get_mean_average() << "\n";
    file.close();
  }
}

int main() {

  FloatValues midterm;

  // show 2 decimal places for every number
  std::cout << std::fixed << std::setprecision(2);

  // midterm.output_all_values();
  // midterm.output_sum();
  // midterm.output_highest_value();
  // midterm.output_lowest_value();
  midterm.output_mean_average();
  // midterm.append_results();

  return 0;
}

// g++ -std=c++17 -o midterm main.cpp
