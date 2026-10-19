#include <iostream>

int main() {
  char char_ex = 'A';

  // increment 30 times, print the char and its ascii value each time
  for (int i = 0; i < 30; i++) {
    char_ex++;
    std::cout << "char: " << char_ex << " , ascii: " << (int)char_ex << "\n";
  }

  return 0;
}

// g++ -std=c++17 -Wall -o char_increment char_increment.cpp
