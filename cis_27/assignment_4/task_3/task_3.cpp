#include <fstream>
#include <iostream>

int main() {
  int i = 0;
  int numbers[1000];
  std::ifstream file("numbers.txt");

  if (file.is_open()) {
    int num;

    while (file >> num) {
      numbers[i] = num;
      i++;
    }
    file.close();
  }

  for (int i = 0; i < 1000; i++) {
    std::cout << numbers[i] * 10 << "\n";
  }

  return 0;
}

// g++ -std=c++17 -o task3 task_3.cpp
