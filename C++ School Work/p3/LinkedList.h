#ifndef LINKED_LIST_H_
#define LINKED_LIST_H_
#include <string>
#include <memory>
#include <sstream>
#include <utility>
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
#endif  // LINKED_LIST_H_
