#include <iostream>
#include <limits>
#include "index_min_pq.h"
#include "Graph.h"
int PrintPath(std::vector<double> dist, std::vector<int> prev,
                   int destination, int source, double weight) {
  std::vector<int> path;
  int pathindex = destination;
  if (dist[pathindex] != std::numeric_limits<double>::max()) {
    while (pathindex != -1) {
      path.push_back(pathindex);
      pathindex = prev[pathindex];
    }
    std::cout << source << " to " << destination << ": ";
    for (int i = path.size()-1; i >= 0; i--) {
      if (i == 0) {
        std::cout << path[i] << " (" << weight << ")" << std::endl;
        return 0;
      }
      std::cout << path[i] << " => ";
    }
  } else {
      std::cout << source << " to " << destination << ": no path" << std::endl;
      return 0;
  }
  return 0;
}
void Dikstra(Graph& g, int source, int destination) {
  IndexMinPQ<double> pq(g.V());
  std::vector<double> dist;
  std::vector<int> prev;
  for (int i = 0; i < g.V(); i++) {
    dist.push_back(std::numeric_limits<double>::max());
    prev.push_back(-1);
  }
  dist[source] = 0;
  pq.Push(dist[source], source);
  while (pq.Size() != 0) {
    int closest = pq.Top();
    pq.Pop();
    if (closest == destination)
      break;
    std::vector<std::pair<int, double>> temp = g.Adj(closest);
    for (auto i : temp) {
      double altpath = dist[closest] + i.second;
      if (altpath < dist[i.first]) {
        dist[i.first] = altpath;
        prev[i.first] = closest;
        if (pq.Contains(i.first)) {
          pq.ChangeKey(dist[i.first], i.first);
        } else {
            pq.Push(dist[i.first], i.first);
        }
      }
    }
  }
  double weight = dist[destination];
  PrintPath(dist, prev, destination, source, weight);
}
int main(int argc, char* argv[]) {
  if (argc != 4) {
    std::cerr << "Usage: ./shortest_path <graph.dat> src dst" << std::endl;
    return 1;
  }
  std::ifstream in(argv[1]);
  if (!in) {
    std::cerr << "Error: cannot open file " << argv[1] << std::endl;
    return 1;
  }
  int numvert;
  if (in >> numvert) {
    Graph g(numvert);
    int v1, v2;
    double w;
    int src = std::atoi(argv[2]);
    int dst = std::atoi(argv[3]);
    // if else block checks if command line arg is valid
    if (src >= numvert || src < 0) {
      std::cerr << "Error: invalid source vertex number " << src << std::endl;
      return 1;
    } else if (dst >= numvert || dst < 0) {
        std::cerr << "Error: invalid dest vertex number " << dst << std::endl;
        return 1;
    }
    while (in >> v1 >> v2 >> w) {
      // if else block checks if numbers in file are valid
      if (v1 >= numvert || v1 < 0) {
        std::cerr << "Invalid source vertex number " << v1 << std::endl;
        return 1;
      } else if (v2 >= numvert || v2 < 0) {
          std::cerr << "Invalid dest vertex number " << v2 << std::endl;
           return 1;
      } else if (w < 0) {
          std::cerr << "Invalid weight " << w << std::endl;
          return 1;
      }
      g.AddEdge(v1, v2, w);
    }
    Dikstra(g, src, dst);
    // else goes with first if, determines if number of verticies is valid
  } else {
      std::cerr << "Error: invalid graph size" << std::endl;
      return 1;
  }
}
