#include <iostream>
#include <string>
#include <memory>
#include <utility>
#include <sstream>
#include <fstream>
#include "binary_tree.h"
class LinkedList {
 public:
  struct List {
    int item;
    std::unique_ptr<List> next;
  };
  int cur_size = 0;
  List* GetNode(int pos);
  LinkedList::List* Get(int pos);
  std::unique_ptr<List> head = nullptr;
  void Insert(int item, int pos);
};
LinkedList::List* LinkedList::GetNode(int pos) {
  List* n = this->head.get();
  while (pos--) n = n->next.get();
    return n;
}
LinkedList::List* LinkedList::Get(int pos) {
  auto n = GetNode(pos);
  return n;
}
void LinkedList::Insert(int item, int pos) {
  auto n = std::unique_ptr<List>(new List);
  n->item = item;
  if (pos == 0) {
    n->next = std::move(head);
    head = std::move(n);
  } else {
      auto prev = Get(pos - 1);
      n->next = std::move(prev->next);
      prev->next = std::move(n);
  }
  cur_size++;
}
template <typename T>
void BuildTree(T& bin, T& val, std::unique_ptr<BinaryTree<int>::Node>& root) {
  if (bin->item == 0) {
    return;
  }
  root = std::unique_ptr<BinaryTree<int>::Node>
                        (new BinaryTree<int>::Node{val->item});
  bin = std::move(bin->next);
  val = std::move(val->next);
  BuildTree(bin, val, root->left);
  bin = std::move(bin->next);
  BuildTree(bin, val, root->right);
}
int main(int argc, char* argv[]) {
  if (argc != 2) {
    std::cerr << "Usage: ./bt_succinct_dec <input_file>" << std::endl;
    return 1;
  }
  std::string input = argv[1];
  std:: ifstream in(input, std::ifstream::in);
  std::string firstline;
  std::string secondline;
  getline(in, firstline);
  if (firstline.empty()) {
    std::cerr << "Error: cannot read structure line" <<std::endl;
    return 1;
  } else if (!(std::isdigit(firstline[0]))) {
      std::cerr << "Error: structure line is invalid" << std::endl;
      return 1;
  }
  getline(in, secondline);
  if (secondline.length() <= 1) {
    std::cerr << "Error: cannot read data line" << std::endl;
    return 1;
  }
  LinkedList binary;
  LinkedList value;
  std::stringstream s1(firstline);
  std::stringstream s2(secondline);
  int token;
  unsigned int count = 0;
  unsigned int ones = 0;
  while (s1 >> token) {
    if (token == 1) {
      binary.Insert(token, count);
      count++;
      ones++;
    } else if (token == 0) {
        binary.Insert(token, count);
        count++;
    } else {
        std::cerr << "Error: structure line is invalid" << std::endl;
        return 1;
    }
  }
  unsigned int count2 = 0;
  while (s2 >> token) {
    value.Insert(token, count2);
    count2++;
  }
  if (count2 < ones) {
    std::cerr << "Error: data line is invalid" << std::endl;
    return 1;
  }
  BinaryTree<int> root;
  BuildTree(binary.head, value.head, root.root);
  root.PreorderPrint();
  root.InorderPrint();
  return 0;
}
