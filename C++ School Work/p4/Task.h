#ifndef TASK_H_
#define TASK_H_

class Task {
 public:
  Task(char, int, int);
  char id;
  unsigned int vruntime = 0;
  unsigned int runtime = 0;
  unsigned int starttime;
  unsigned int duration;
};
Task::Task(char id, int s, int d): id(id), starttime(s), duration(d) {}
#endif  // TASK_H_
