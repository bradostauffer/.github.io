
CXX := g++
CXXFLAGS = -Wall -Werror -std=c++11
all: shortest_path

shortest_path:shortest_path.o
	-$(CXX) -o $@ $^
clean:
	-rm -f *.o shortest_path
