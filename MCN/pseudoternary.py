import matplotlib.pyplot as plt
def pseudoternary(bits, voltage):
    time = [0]
    signal = [0]
    t = 0
    last = -voltage
    for bit in bits:
        if bit == '0':
            last = voltage if last == -voltage else -voltage
            level = last
        else:
            level = 0
        time.append(t)
        signal.append(level)
        time.append(t + 1)
        signal.append(level)
        t += 1

    plt.plot(time, signal,color='blue')
    plt.title("Pseudoternary Encoding")
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.grid(True)
    plt.axhline(0, color='green')
    plt.axvline(0, color='green')
    plt.show()
bits = input("Enter Data Bit: ")
voltage = float(input("Enter Voltage: "))
pseudoternary(bits, voltage)