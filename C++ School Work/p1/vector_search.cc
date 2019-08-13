#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <memory>
#include <chrono>
#include <cmath>
#include <exception>
class Point {
 public:
  explicit Point(std::string s) {
     std::stringstream ss(s);
     int count = 0;
     // seeing how many bumber in file to detrmine if its a vector or mag file
     for (unsigned int i = 0; i < s.length(); i++) {
       if (s[i] == ' ') {
         count++;
       }
     }
    if (count == 0) {
      ss >> sepmag;
    } else if (count == 1) {
        ss >> x;
        ss >> y;
    }
  }
  int getx()const {
    return x;
  }
  int gety()const {
    return y;
  }
  int getmag() {
    mag = sqrt((x*x) + (y*y));
    return mag;
  }
  int getsepmag()const {
    return sepmag;
  }

 private:
  int x;
  int y;
  int mag;  // mag is the calculated magnitude from vector file
  int sepmag;  // semeg is the magnitude from magnitude file
};
class Clock {
 public:
  void Reset() {
    start = std::chrono::high_resolution_clock::now();
  }
  void CurrentTime() {
    end = std::chrono::high_resolution_clock::now();
  }double End() {
    elapsed = std::chrono::duration<double, std::micro>(end-start).count();
    return elapsed;
  }

 private:
  std::chrono::high_resolution_clock::time_point start;
  std::chrono::high_resolution_clock::time_point end;
  double elapsed;
};


template <class T>
std::vector<T> vec_read(std::string filename) {
  std::vector<T> vec;
  std::string tmp;
  std::ifstream in(filename);
  if (in.is_open()) {
  while (getline(in, tmp)) {
    vec.push_back(new Point(tmp));  // object pointers less memory
                                    // than vec of objects
  }
  }
    return vec;
}
// predicate function for std::sort, overload doesn't work with object ptr
// I had to make decision over less memory for vec of object ptr
// over using overload
bool Compare(Point* a, Point* b) {
  if (a->getmag() == b->getmag()) {
    return (a->gety() < b->gety());
  } else {
      return (a->getmag() < b->getmag());
  }
}
template <class T>
int LinearSearch(std::vector<T> pointvec, std::vector<T> magvec) {
  int count = 0;
  for (unsigned int i = 0; i < magvec.size(); i++) {
    for (unsigned int j = 0; j < pointvec.size(); j++) {
      if (magvec[i]->getsepmag() == pointvec[j]->getmag()) {
        count++;
        break;
      }
    }
  }
  return count;
}

template <class T>
int BinarySearch(std::vector<T> pointvec, int key) {
  int count = 0;
    int lo = 0, hi = pointvec.size()-1;
    while (lo <= hi) {
      int mid = lo + (hi  - lo) / 2;
      if (pointvec[mid]->getmag() == key) {
       count++;
       return count;
      }
     if (pointvec[mid]->getmag() < key) {
       lo = mid +1;
     } else {
         hi = mid - 1;
     }
    }
    return count;
}


int main(int argc, char *argv[]) {
  int count = 0;
  Clock ct;
  // making sure correct # of arguments
  if (argc > 4 || argc <= 3) {
    std::cout << "Usage: ./vector_search <vector_file.dat>"
                "<magnitude_file.dat> <result_file.dat>" << std::endl;
    std::cerr << "Usage: ./vector_search <vector_file.dat>"
                " <magnitude_file.dat> <result_file.dat>" << std::endl;
    return 1;
  }
  // opening file to write count in
  std::string filename = argv[3];
  std::ofstream myfile;
  myfile.open(filename);
  // making arguments 1,2, and 3 strings to check for .dat extension
  std::string ar1 = argv[1];
  std::string ar2 = argv[2];
  std::string ar3 = argv[3];
  std::vector<Point*>pvec =  vec_read<Point*> (argv[1]);
  std::vector<Point*>mvec = vec_read<Point*>(argv[2]);
  std::size_t find = ar1.find(".dat");
  std::size_t found = ar2.find(".dat");
  std::size_t look = ar3.find(".dat");
  if (pvec.empty()) {
    std::cout << "Error: cannot open file " << argv[1] << std::endl;
    std::cerr << "Error: cannot open file " << argv[1] << std::endl;
    myfile << "Error: cannot open file " << argv[1];
    return 1;
  } else if (mvec.empty()) {
      std::cout << "Error: cannot open file " << argv[2] << std::endl;
      std::cerr << "Error: cannot open file " << argv[2] << std::endl;
      myfile << "Error: cannot open file " << argv[2];
      return 1;
  } else if (find == std::string::npos) {
      std::cout << "Error: cannot open file " << argv[1] << std::endl;
      std::cerr << "Error: cannot open file " << argv[1] << std::endl;
      myfile << "Error: cannot open file " << argv[1];
      return 1;
  } else if (found == std::string::npos) {
      std::cout << "Error: cannot open file " << argv[2] << std::endl;
      std::cerr << "Error: cannot open file " << argv[2] << std::endl;
      myfile << "Error: cannot open file " << argv[2];
      return 1;
  } else if (look == std::string::npos) {
      std::cout << "Error: cannot open file " << argv[3] << std::endl;
      std::cerr << "Error: cannot open file " << argv[3] << std::endl;
      myfile << "Error: cannot open file " << argv[3];
      return 1;
    }
  char choice;
  std::sort(pvec.begin(), pvec.end(), Compare);
  int loopcount = 0;
  while (!loopcount) {
    std::cout << "Choice of search method ([l]inear, [b]inary)?" << std::endl;
    std::cin >> choice;
    ct.Reset();
    switch (choice) {
     case 'l':
     case 'L':
       count = LinearSearch(pvec, mvec);
       loopcount = 2;
       break;
     case 'b':
     case 'B':
       for (unsigned int i = 0; i < mvec.size(); i++)
         count+= BinarySearch(pvec, mvec[i]->getsepmag());
       loopcount = 2;
       break;
     default:
       std::cerr << "Incorrect choice" << std::endl;
       std::cin.clear();
       std::cin.ignore();
       break;
    }
  }
  ct.CurrentTime();
    std::cout <<"CPU time: " << ct.End()<< " microseconds" <<std::endl;
    myfile << count;
    myfile.close();
    return 0;
}
