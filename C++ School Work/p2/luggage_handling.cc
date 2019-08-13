#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <fstream>
#include <streambuf>
template <class T>
class Stack {
 public:
  unsigned int Size();
  T& Top();
  void Pop();
  void Push(const T& item);
 private:
  std::vector<T> items;
};
template <class T>
unsigned int Stack<T>::Size() {
  return items.size();
}
template <class T>
T& Stack<T>::Top(void) {
  if (!Size())
    throw std::underflow_error("Empty stack!");
  return items.back();
}
template <class T>
void Stack<T>::Pop() {
  if (!Size())
    throw std::underflow_error("Empty stack!");
  items.pop_back();
}
template <class T>
void Stack<T>::Push(const T& item) {
  items.push_back(item);
}
template <typename T>
class Queue {
 public:
  unsigned int Size();
  T& Front();
  T& Back();
  void Pop();
  void Push(const T& item);
 private:
  std::list<T> items;
};
template <typename T>
unsigned int Queue<T>::Size() {
  return items.size();
}
template <typename T>
T& Queue<T>::Front() {
  if (!Size())
    throw std::underflow_error("Empty queue");
  return items.front();
}
template <typename T>
T& Queue<T>::Back() {
  if (!Size())
    throw std::underflow_error("Empty queue!");
  return items.back();
}
template <typename T>
void Queue<T>::Pop() {
  if (!Size())
    throw std::underflow_error("Empty queue");
  items.pop_front();
}
template <typename T>
void Queue<T>::Push(const T& item) {
  items.push_back(item);
}
// this creates the queue that wll be stored in a stack
Queue<int> Queuemake(std::vector<int> v, int position, int numbags) {
  Queue<int> foo;
  for (int i = position; i < (numbags+position); i++) {
    unsigned int j = i;
    if (j  == v.size())
      break;
    foo.Push(v[i]);
  }
  return foo;
}
int main(int argc, char* argv[]) {
  Stack<Queue<int>> s;
  std::vector<int> bags;
  int bag;
  unsigned int pos = 0;
  std::string token;
  if (argc != 3) {
    std::cerr << "Usage: ./luggage_handling <input_file> <container_size>"
              << std::endl;
              return 1;
  }
  std::string tmp = argv[2];
  std::string input = argv[1];
  std::ifstream myfile(input);
  if (!myfile) {
    std::cerr << "Error: cannot open file " << argv[1] << std::endl;
    return 1;
  }
  int numbags = std::stoi(tmp);
  if (numbags < 1) {
    std::cerr << "Error: invalid container size" <<std::endl;
    return 1;
  }
  std::string line;
  // tokenizes and stores strings in vector
  while (myfile.good()) {
  getline(myfile, line);
    std::stringstream is(line);
    std::string token;
    while (getline(is, token, ' ')) {
    if (std::stoi(token)) {
     bag = std::stoi(token);
     bags.push_back(bag);
     } else {
         return 1;
       }
  }
  }
  // this makes a stack of queue objects
  // the pos increases to make sure the correct # of bags are in the queue
  while (1) {
    if (pos > bags.size())
      break;
    s.Push(Queuemake(bags, pos, numbags));
    pos += numbags;
  }
  // this prints out the bags in the correct order
  while (s.Size() != 0) {
    if ((s.Top()).Size() != 0) {
      std::cout << (s.Top()).Front() << " ";
       (s.Top()).Pop();
     } else {
         s.Pop();
       }
  }
  // a new line just for the autograder
  std::cout << std::endl;
}
