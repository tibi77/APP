import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = [2,4,6,8,10,12,14,16]

t2 =  [24.538,13.951, 9.310,10.972, 8.239, 7.211, 6.994, 7.441]
t1 =  [20.538,10.951, 9.010,9.072, 8.769, 8.621, 8.384, 8.441]

fig, ax = plt.subplots()

plt.plot(x, t1, "-b", label="Ibm-dp.q wn01")
plt.plot(x, t2, "-p", label="ibm_nehalem.q")
plt.legend(loc="upper left")

ax.set(xlabel='parallel unit', ylabel='time(s)',
       title='MPI_OPENMP 4 threads')

ax.grid()
plt.show()
