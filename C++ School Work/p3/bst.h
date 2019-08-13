#ifndef BST_H_
#define BST_H_

#include <algorithm>
#include <iostream>
#include <memory>
#include <utility>
#include <stack>
#include <queue>
#include <sstream>
/*
 * Class definition
 */
template <typename T>
class BST {
 public:
  /* Return floor key in tree */
  const T& floor(const T &key);
  /* Return ceil key in tree */
  const T& ceil(const T &key);
  /* Return k-th smallest key in tree */
  const T& kth_small(const int kth);

  /* Return whether @key is found in tree */
  bool contains(const T& key);

  /* Return max key in tree */
  const T& max();
  /* Return min key in tree */
  const T& min();

  /* Insert @key in tree */
  void insert(const T &key);
  /* Remove @key from tree */
  void remove(const T &key);

  /* Print tree in-order */
  void print();

 private:
  struct Node{
    T key;
    std::unique_ptr<Node> left;
    std::unique_ptr<Node> right;
  };
  std::unique_ptr<Node> root;

  /* Useful recursive helper methods */
  Node* min(Node *n);
  void recur_inorder(Node* n, std::queue<T>& q);
  void insert(std::unique_ptr<Node> &n, const T &key);
  void remove(std::unique_ptr<Node> &n, const T &key);
  void print(Node *n, int level);
};

/*
 * Implementation
 */
template <typename T>
void BST<T>::recur_inorder(Node* n, std::queue<T>& q) {
  if (!n) return;
  recur_inorder(n->left.get(), q);
  q.push(n->key);
  recur_inorder(n->right.get(), q);
}
template <typename T>
const T& BST<T>::floor(const T &key) {
  std::stack<T> s;
  static T tmp1;
  if (!root) {
    std::stringstream s;
    s << "Empty tree";
    throw std::invalid_argument(s.str());
  } else if (contains(key)) {
      tmp1 = key;
      return tmp1;
  } else if (key < min()) {
      std::stringstream s;
      s << "Cannot find floor for key " << key;
      throw std::invalid_argument(s.str());
  }
  insert(key);
  Node* n = root.get();
  while (n) {
    if (key == n->key) {
      tmp1 = s.top();
      break;
    } else if (key < n->key) {
        n = n->left.get();
    } else {
        s.push(n->key);
        n = n->right.get();
    }
  }
  if (tmp1 > key) {
    std::stringstream s;
    s << "Cannot find floor for key " << key;
    throw std::invalid_argument(s.str());
  }
  remove(root, key);
  return tmp1;
}

template <typename T>
const T& BST<T>::ceil(const T &key) {
  std::stack<T> s;
  static T tmp;
  if (!root) {
    std::stringstream s;
    s << "Empty tree";
    throw std::invalid_argument(s.str());
  } else if (contains(key)) {
    tmp = key;
    return tmp;
  } else if (key > max()) {
      std::stringstream s;
      s << "Cannot find ceil for key " << key;
      throw std::invalid_argument(s.str());
  }
//  insert(key);
  Node* n = root.get();
  while (n) {
    if (key == n->key) {
      tmp = s.top();
      break;
    } else if (key < n->key) {
        s.push(n->key);
        n = n->left.get();
    } else {
        n = n->right.get();
    }
  }
  if (tmp < key) {
  std::stringstream s;
  s << "Cannot find ceil for key " << key;
  throw std::invalid_argument(s.str());
  }
  //remove(root, key);
  return tmp;
}

template <typename T>
const T& BST<T>::kth_small(const int kth) {
  std::queue<T> q;
  static T tmp;
  recur_inorder(root.get(), q);
  if (kth <= 0) {
    std::stringstream s;
    s << "Cannot find " << kth <<"th element";
    throw std::invalid_argument(s.str()); tmp = q.front();
  }
  unsigned int compare = kth;
  if (q.size() < compare) {
    std::stringstream s;
    s << "Cannot find " << kth <<"th element";
    throw std::invalid_argument(s.str());
  }
  int count = 0;
  while (count < kth-1) {
    count++;
    q.pop();
  }
  if (kth == 0) {
    std::stringstream s;
    s << "Cannot find " << kth <<"th element";
    throw std::invalid_argument(s.str()); tmp = q.front();
  }
    tmp = q.front();
    return tmp;
}

/*
 * @@@ Code below should not be modified @@@
 */
template <typename T>
bool BST<T>::contains(const T &key) {
  Node *n = root.get();

  while (n) {
    if (key == n->key)
      return true;

    if (key < n->key)
      n = n->left.get();
    else
      n = n->right.get();
  }

  return false;
}

template <typename T>
const T& BST<T>::max(void) {
  if (!root) throw std::runtime_error("Empty tree");
  Node *n = root.get();
  while (n->right) n = n->right.get();
  return n->key;
}

template <typename T>
const T& BST<T>::min(void) {
  return min(root.get())->key;
}
template <typename T>
typename BST<T>::Node* BST<T>::min(Node *n) {
  if (n->left)
    return min(n->left.get());
  else
    return n;
}

template <typename T>
void BST<T>::insert(const T &key) {
  insert(root, key);
}

template <typename T>
void BST<T>::insert(std::unique_ptr<Node> &n, const T &key) {
  if (!n)
    n = std::unique_ptr<Node>(new Node{key});
  else if (key < n->key)
    insert(n->left, key);
  else if (key > n->key)
    insert(n->right, key);
  else
    std::cerr << "Key " << key << " already inserted!\n";
}

template <typename T>
void BST<T>::remove(const T &key) {
  remove(root, key);
}

template <typename T>
void BST<T>::remove(std::unique_ptr<Node> &n, const T &key) {
  /* Key not found */
  if (!n) return;

  if (key < n->key) {
    remove(n->left, key);
  } else if (key > n->key) {
    remove(n->right, key);
  } else {
    /* Found node */
    if (n->left && n->right) {
      /* Two children: replace with min node in right subtree */
      n->key = min(n->right.get())->key;
      remove(n->right, n->key);
    } else {
      /* Replace with only child or with nullptr */
      n = std::move((n->left) ? n->left : n->right);
    }
  }
}

template <typename T>
void BST<T>::print() {
  if (!root) return;
  print(root.get(), 1);
  std::cout << std::endl;
}

template <typename T>
void BST<T>::print(Node *n, int level) {
  if (!n) return;

  print(n->left.get(), level + 1);
  std::cout << n->key
      << " (" << level << ") ";
  print(n->right.get(), level + 1);
}

#endif /* BST_H_ */
