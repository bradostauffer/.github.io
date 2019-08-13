#include <algorithm>
#include <iostream>
#include <random>
#include <vector>

#include "bst.h"

int main() {
  std::vector<int> keys{51, 43, 93, 18, 42, 99, 54, 2, 74};

  BST<int> bst;

  try {
    bst.ceil(42);
  } catch (std::exception &e) {
    std::cout << "Expected exception: " << e.what() << std::endl;
  }

  for (auto i : keys)
    bst.insert(i);

  /* Test floor */
  std::cout << "ceil(54) = " << bst.ceil(54) << "\n";
  std::cout << "ceil(55) = " << bst.ceil(55) << "\n";
  try {
    bst.ceil(100);
  } catch (std::exception &e) {
    std::cout << "Expected exception: " << e.what() << std::endl;
  }

  /* Test ceil */
  std::cout << "floor(54) = " << bst.floor(54) << "\n";
  std::cout << "floor(55) = " << bst.floor(55) << "\n";

  /* Test kth_small */
  std::cout << "kth(1) = " << bst.kth_small(1) << "\n";
  std::cout << "kth(5) = " << bst.kth_small(5) << "\n";

  return 0;
}
