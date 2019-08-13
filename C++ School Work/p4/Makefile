CXXFLAGS = -Wall -Werror -std=c++11
all: cfs_sched

cfs_sched:cfs_sched.o
	$(CXX) -o $@ $^
clean:
	rm -f *.o cfs_sched
