CXXFLAGS=-Wall -Werror
all: vector_search

vector_search: vector_search.o
	$(CXX) -std=c++11 -o $@ $^	
clean:
	rm -f *o vector_search
	rm -f *.dat
