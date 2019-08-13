#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include "llrb_multimap.h"
#include "Task.h"
bool Compare(Task* a, Task* b) {
  if (a->id < b->id)
    return true;
  else
    return false;
}
int main(int argc, char* argv[]) {
LLRB_multimap<int, Task*> tree;
char id;
int d;
int s;
int timelinesize = 0;
if (argc != 2) {
  std::cerr << "Usage: ./cfs_sched <task_file.dat>" << std::endl;
  return 1;
}
std::vector<Task*> taskvec;
std::ifstream in(argv[1]);
if (!in) {
  std::cerr << "Error: cannot open file " << argv[1] << std::endl;
  return 1;
}
while (in >> id >> d >> s) {
  taskvec.push_back(new Task(id, d, s));
}
std::sort(taskvec.begin(), taskvec.end(), Compare);
Task* task = nullptr;
unsigned int tick = 0;
unsigned int minvruntime = 0;
unsigned int taskcount = 0;
while (true) {
  // for loop finds what to put in timeline
  for (unsigned int i = 0; i < taskvec.size(); i++) {
    if (tick == taskvec[i]->starttime) {
      taskvec[i]->vruntime = minvruntime;
      // inserting with correct start time in timeline
      tree.Insert(taskvec[i]->vruntime, taskvec[i]);
      timelinesize++;
    }
  }
  // if all the tasks are complete
  if (taskcount == taskvec.size()) {
    break;
    // an empty tree
  } else if (tree.Size() == 0 && task == nullptr) {
      std::cout << tick << " " << "[" << timelinesize << "]:" <<  " _" << std::endl;
      tick++;
      continue;
  }
  // none currently working on
  if (!task) {
    task = tree.Get(tree.Min());
    tree.Remove(task->vruntime);
  }
  if (task->vruntime > minvruntime) {
    tree.Insert(task->vruntime, task);
    task = tree.Get(tree.Min());
    tree.Remove(task->vruntime);
  }  // task now begins to run
  task->runtime++;
  task->vruntime++;
  // if the tree is empty
  if (tree.Size() == 0) {
    minvruntime = task->vruntime-1;
  } else {
      minvruntime = tree.Min();
  }
  // current task is done
  if (task->runtime == task->duration) {
    std::cout << tick << " " << "[" << timelinesize << "]:" <<
                  " "  << task->id << "*" << std::endl;
    taskcount++;
    timelinesize--;
    task = nullptr;
    // regular print at end of tick
  } else if (task->runtime < task->duration) {
    std::cout << tick << " " << "[" << timelinesize <<"]:" << " " <<
                                       task->id << std::endl;
  }
  tick++;
}
// destructor for all Task*
  for (auto i : taskvec) {
    delete i;
  }
}
