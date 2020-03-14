import numpy as np
import matplotlib.pyplot as plt

def euler(P_init, G_init, Dt): 
    t_init = 0
    t_end = 100
    n_steps = int(round((t_end-t_init)/Dt))
    
    P_arr = np.zeros(n_steps + 1)
    G_arr = np.zeros(n_steps + 1)
    t_arr = np.zeros(n_steps + 1)

    P_arr[0] = P_init #initial value of rainbow fish
    G_arr[0] = G_init #initial value of aggressive fish
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
    
    plt.plot(P_arr, G_arr, linewidth = 4)

D = 1/8
euler(20, 5, D)
euler(1, 30, D)
euler(120, 1, D)

plt.title("P/G graph", fontsize = 20)
plt.axis([0,120,0,30])

plt.show()
