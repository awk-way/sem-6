import matplotlib.pyplot as plt
def differential_manchester(data):
    time = []
    signal = []
    t = 0
    prev_level = 1   # starting level

    for bit in data:
        if bit == '0':
            prev_level = 1 - prev_level   # transition at start
        first_half = prev_level
        second_half = 1 - prev_level      # mid-bit transition
        for level in [first_half, second_half]:
            time.extend([t, t+1])
            signal.extend([level, level])
            t += 1
        prev_level = second_half
    return time, signal

data = input("Enter binary string: ")
time, signal = differential_manchester(data)
plt.step(time, signal, where='post')
plt.ylim(-0.5, 1.5)
plt.yticks([0,1], ["LOW","HIGH"])
plt.xlabel("Time")
plt.ylabel("Signal Level")
plt.title("Differential Manchester Encoding")
plt.grid(True)
plt.show()