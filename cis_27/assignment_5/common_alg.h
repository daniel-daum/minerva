

class Common_Alg {
private:
  int *numbers;
  int size;

public:
  // constructor: fill array from numbers.txt
  Common_Alg();

  // destructor: free dynamic array
  ~Common_Alg();

  void output_all_values();
  void output_sum_all_values();
  void output_all_odd();
  void output_all_even();
  void binary_search(int num);
  void output_middle_value();
  void output_first_value();
  void output_last_value();
  void output_highest_value_loc();
  void output_lowest_value_loc();
  void bubble_sort();
  void output_bubble_sort();
  void mean_average();
};


