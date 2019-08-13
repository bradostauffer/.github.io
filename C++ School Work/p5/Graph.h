#ifndef GRAPH_H_
#define GRAPH_H_
#include <fstream>
#include <utility>
#include <vector>
#include <algorithm>
class Graph {
 private:
  std::vector<std::vector<std::pair<int, double>>> adj_list;
  int numvert;
  int numedge = 0;
 public:
  explicit Graph(int v);
  // return number of verticies
  int V();
  // returns number of edges
  int E();
  // returns vector of adjacent edges
  std::vector<std::pair<int, double>> Adj(int v);
  // creates edges
  void AddEdge(int v1, int v2, double w);
};
#endif  // GRAPH_H_

Graph::Graph(int v): adj_list(v), numvert(v) {}
void Graph::AddEdge(int v1, int v2, double w) {
  adj_list[v1].emplace_back(std::make_pair(v2, w));
  ++numedge;
}
std::vector<std::pair<int, double>> Graph::Adj(int v) {
  return adj_list[v];
}
int Graph::V() {
  return numvert;
}
int Graph::E() {
  return numedge;
}
