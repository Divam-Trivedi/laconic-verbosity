import numpy as np


t = [[[1,2,3,4,5], [6,7,8]], [[1,2,3,4,5], [6,7,8]], [[1,2,3,4,5], [6,7,8]]]
for i in range(len(t)):
    for j in range(len(t[i])):
        for k in range(len(t[i][0]) - len(t[i][1])):
            print(k)
            t[i][1].append(9)
        # for k in range(len(t[i][j]))
print((t))
t=np.array