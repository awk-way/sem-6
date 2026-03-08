import matplotlib.pyplot as plt
def manchester_encode(data):
    time = []
    signal = []
    t = 0
    for bit in data:
        if bit == '0':
            levels = [0, 1]   # Low -> High
        else:
            levels = [1, 0]   # High -> Low
        for level in levels:
            time.extend([t, t+1])
            signal.extend([level, level])
            t += 1
    return time, signal

data = input("Enter binary string: ")
time, signal = manchester_encode(data)
plt.step(time, signal, where='post')
plt.ylim(-0.5, 1.5)
plt.yticks([0,1], ["LOW","HIGH"])
plt.xlabel("Time")
plt.ylabel("Signal Level")
plt.title("Manchester Encoding")
plt.grid(True)
plt.show()