import numpy as np
import matplotlib.pyplot as plt

def euler(Dt): 
    t_init = 0
    t_end = 100
    n_steps = int(round((t_end-t_init)/Dt))
    
    P_arr = np.zeros(n_steps + 1)
    G_arr = np.zeros(n_steps + 1)
    t_arr = np.zeros(n_steps + 1)

    P_arr[0] = 20 #initial value of rainbow fish
    G_arr[0] = 5 #initial value of aggressive fish
    t_arr[0] = t_init
    
    for i in range (1, n_steps + 1):
        P = P_arr[i-1]
        G = G_arr[i-1]
        t = t_arr[i-1]
        dPdt = 0.7 * P - 0.007 * P * P - 0.04 * P * G
        dGdt = -0.25 * G + 0.008 * P * G
        P_arr[i] = P + Dt * dPdt
        G_arr[i] = G + Dt * dGdt
        t_arr[i] = t + Dt
    
    #result = np.where(P_arr == np.amax(P_arr))
    #result = np.amax(P_arr)
    index = int(6 / Dt)
    return P_arr[index]

err = 2
i = 1
while err > 1:
    i = i/2
    err = abs(euler(i) - euler(2*i))
    print(1/i, euler(i), euler(2*i), err)

print(i, err)
