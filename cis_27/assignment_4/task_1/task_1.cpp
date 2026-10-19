// g++ -std=c++17 -o task1 task_1.cpp
#include <fstream>
#include <iostream>
#include <random>

void write_to_file() {

  // setup random number generation from <random>
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_int_distribution<int> dist(1, 1000);

  int numbers[10000];

  // generate numbers, add to an array
  for (int i = 0; i < 1000; i++) {
    numbers[i] = dist(gen);
    std::cout << numbers[i];
  };

  std::ofstream file("numbers.txt");

  // print to file
  if (file.is_open()) {
    for (int i = 0; i < 1000; i++) {
      file << numbers[i] << "\n";
    }
    file.close();
  }
}

int main() {
  write_to_file();
  return 0;
}
