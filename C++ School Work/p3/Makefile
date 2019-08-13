CXXFLAGS=-Wall -Werror
all: bt_succinct_dec bst_tester
bt_succinct_dec: bt_succinct_dec.o
	$(CXX) -std=c++11 -o $@ $^
bst_tester: bst_tester.o
	$(CXX) -std=c++11 -o $@ $^
clean:
	rm -f *.o bt_succinct_dec bst_tester
