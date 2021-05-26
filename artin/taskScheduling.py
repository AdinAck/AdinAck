# TIN TIN THE VG KID
class Task:
    def __init__(self, start, end, value):
        self.start, self.end, self.value = start, end, value

# example = (Task(0, 5, 10),
#            Task(3, 7, 15),
#            Task(5, 8, 3))

# example = (Task(1, 2, 50),
#            Task(3, 5, 20),
#            Task(6, 19, 100),
#            Task(2, 100, 200))

example = (Task(0, 6, 60),
           Task(1, 4, 30),
           Task(3, 5, 10),
           Task(5, 7, 30),
           Task(5, 9, 50),
           Task(7, 8, 10))

example = sorted(example, key=lambda task: task.end)

def latestNonConflictingTask(index):
    for i, task in enumerate(example[:index][::-1]):
        if task.end <= example[index].start:
            return index-i-1

    return -1

def r(index):
    if index == 0:
        return example[0].value
    # determine latest nonconflicting task
    inclusive = example[index].value
    lnct = latestNonConflictingTask(index)
    if lnct != -1:
        inclusive += r(lnct)

    return max(inclusive, r(index-1))

def r2(index):
    if index == 0:
        return example[0].value

    here = example[index].value

    # determine latest nonconflicting task
    if (lnct := latestNonConflictingTask(index)) == -1:
        return max(here, r2(index-1))
    else:
        return max(here+r(lnct), r2(index-1))



print(r(len(example)-1))
print(r2(len(example)-1))
