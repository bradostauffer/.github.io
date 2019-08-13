CXXFLAGS=-Wall -Werror
all: postfix_eval luggage_handling

postfix_eval: postfix_eval.o
	$(CXX) -std=c++11 -o $@ $^
luggage_handling: luggage_handling.o
	$(CXX) -std=c++11 -o $@ $^
clean:
	rm -f *.o postfix_eval luggage_handling
