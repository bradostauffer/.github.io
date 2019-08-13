#include <iostream>
#include <string>
#include <sstream>
#include <vector>
template <typename T>
class Stack {
 public:
  unsigned int Size();
  T& Top();
  void Pop();
  void Push(const T& item);
 private:
  std::vector<T> items;
};
template <typename T>
unsigned int Stack<T>::Size() {
  return items.size();
}
template <typename T>
T& Stack<T>::Top(void) {
  if (!Size())
    throw std::underflow_error("Empty stack!");
  return items.back();
}
template <typename T>
void Stack<T>::Pop() {
  if (!Size())
    throw std::underflow_error("Empty stack!");
  items.pop_back();
}
template <typename T>
void Stack<T>::Push(const T& item) {
  items.push_back(item);
}
double CharOp(double a, double b, std::string s) {
  char op = s[0];
  switch (op) {
    case '+':
      return (a + b);
      break;
    case '-':
      return (a - b);
      break;
    case '*':
      return (a * b);
      break;
    case '/':
      return (a / b);
      break;
    default:
      return 0;
  }
}
int main() {
  Stack<double> nums;
  std::string input;
  double total = 0;
  double tmpa, tmpb, stackval;
  int error = 0;  //  0 meaning error already called, 1 being already called
                  //  this prevents the same error appearing twice
  std::string token;
    error = 0;
  // takes input from cin and tokenizes it at the appearance of whitespace.
  while (getline(std::cin, input)) {
    std::stringstream ss(input);
    while (getline(ss, token, ' ')) {
      try {
        if (std::stod(token)) {
        stackval = std::stod(token);
        nums.Push(stackval);
        }
    } catch(std::exception& e) {
        if (token == "+" || token == "-" || token == "*" || token == "/") {
          if (nums.Size() == 1) {
            std::cerr << "Error: invalid expression" << std::endl;
            error = 1;
            break;
          }
          // takes top two numbers and the operator and gives it to operator
          // function so the operation can take place
          tmpa = nums.Top();
          nums.Pop();
          tmpb = nums.Top();
          nums.Pop();
          total = CharOp(tmpb, tmpa, token);
          nums.Push(total);
        } else {
            std::cerr << "Error: unknown symbol '" << token << "'" << std::endl;
            error = 1;
          }
       }
     ss.clear();
    }
    if (nums.Size() == 1 && error != 1) {
      total = nums.Top();
      nums.Pop();
      std::cout << total << std::endl;
    } else if (error == 1) {
      continue;
      } else {
          std::cerr << "Error: invalid expression" << std::endl;
        }
  }
  std::cout <<"Bye!" << std::endl;
}
