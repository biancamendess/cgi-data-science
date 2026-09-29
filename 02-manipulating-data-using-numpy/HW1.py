import numpy as np

a = np.array([1, 5, 10, 3, 4, 25, 30])
b = np.array([11, 15, 20, 21, 35, 40, 45])

def homework(a):
    my_result = a[(a % 5 == 0) & (a% 2 == 1)]
    return my_result

your_answer = homework(b)

print("Your answer:", your_answer)