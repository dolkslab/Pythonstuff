import numpy as np
import custom_math as cst_math
import color
import math
import cow
import time





def get_distance():
    dt = 0.0001
    cow_sim = cow.cow_sprite(0,np.array([0.,60.]),10.,0.,60.,0.5,10200.)
    cow_sim.state = 1
    t = 0.
    while cow_sim.state != 3:
        sim_out = cow_sim.update(dt)
        t += dt
    print(t)
    return sim_out

times = np.array([])
for i in range(1):
    t_0_bench = time.time()
    print_out = get_distance()
    t_1_bench = time.time()
times = np.append(times, t_1_bench - t_0_bench)

t_avg = np.average(times)
print(t_avg)
print(print_out[1][0])
print(cst_math.mag(print_out[2]))


