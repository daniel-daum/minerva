#include <iostream>

const int MAX_SIZE = 256;

class My_String {
private:
  char input_buffer[MAX_SIZE];
  char original[MAX_SIZE];

public:
  // constructor: copy the input char by char into input_buffer 
  My_String(const char input[]) {
    int i = 0;

    while (i < MAX_SIZE - 1 && input[i] != '\0') {
      input_buffer[i] = input[i];
      original[i] = input[i];
      i++;
    }
    input_buffer[i] = '\0';
    original[i] = '\0';
  }

  // method 1: count characters until '\0'
  int length() {
    int count = 0;

    for (;;) {
      if (input_buffer[count] == '\0') {
        break;
      }
      count++;
    }
    return count;
  }

  // method 2: check if the string is all letters
  bool is_alpha() {
    bool all_letters = true;

    for (int i = 0; input_buffer[i] != '\0'; i++) {
      char c = input_buffer[i];

      // A-Z is 65-90, 
      // a-z is 97-122
      if (!((c >= 65 && c <= 90) || (c >= 97 && c <= 122))) {
        std::cout << "not a letter at index " << i << ": '" << c << "'\n";
        all_letters = false;
      }
    }

    if (all_letters) {
      std::cout << "string is all letters\n";
    } else {
      std::cout << "string is not all letters\n";
    }
    return all_letters;
  }

  // method 3: convert a-z to A-Z by subtracting 32
  void to_upper() {
    for (int i = 0; input_buffer[i] != '\0'; i++) {
      if (input_buffer[i] >= 97 && input_buffer[i] <= 122) {
        input_buffer[i] = input_buffer[i] - 32;
      }
    }
    std::cout << input_buffer << "\n";
  }

  // method 4: convert A-Z to a-z by adding 32
  void to_lower() {
    for (int i = 0; input_buffer[i] != '\0'; i++) {
      if (input_buffer[i] >= 65 && input_buffer[i] <= 90) {
        input_buffer[i] = input_buffer[i] + 32;
      }
    }
    std::cout << input_buffer << "\n";
  }

  // method 5: put c where '\0' was, then add a new '\0' after it
  void push_back(char c) {
    int end = length();

    // last slot is saved for '\0'
    if (end >= MAX_SIZE - 1) {
      std::cout << "buffer is full, can't add " << c << "\n";
      return;
    }

    input_buffer[end] = c;
    input_buffer[end + 1] = '\0';
    std::cout << input_buffer << "\n";
  }

  // method 6: output original string
  void output_original() { std::cout << "original: " << original << "\n"; }

  // method 7: output current string
  void output_current() { std::cout << "current: " << input_buffer << "\n"; }
};

int main() {
  char input[MAX_SIZE];

  std::cout << "enter a string: ";
  std::cin.getline(input, MAX_SIZE);

  // input was longer than the buffer: keep what fit, drop the rest
  if (std::cin.fail()) {
    std::cin.clear();
    std::cin.ignore(10000, '\n');
  }

  My_String my_string(input);
  my_string.output_original();

  int choice = -1;

  while (choice != 0) {
    std::cout << "\n----- menu -----\n";
    std::cout << "1. length\n";
    std::cout << "2. is alpha\n";
    std::cout << "3. to upper\n";
    std::cout << "4. to lower\n";
    std::cout << "5. push back\n";
    std::cout << "6. show original and current\n";
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
      std::cout << "length: " << my_string.length() << "\n";
      break;
    case 2:
      my_string.is_alpha();
      break;
    case 3:
      my_string.to_upper();
      break;
    case 4:
      my_string.to_lower();
      break;
    case 5: {
      char c;
      std::cout << "enter one character: ";
      std::cin >> c;
      std::cin.ignore(10000, '\n');
      my_string.push_back(c);
      break;
    }
    case 6:
      my_string.output_original();
      my_string.output_current();
      break;
    case 0:
      break;
    default:
      std::cout << "invalid choice\n";
    }
  }

  return 0;
}

// g++ -std=c++17 -Wall -o my_string my_string.cpp
