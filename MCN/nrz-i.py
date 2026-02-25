import matplotlib.pyplot as plt
def nrz_i(bits, voltage):
    time = [0]
    signal = []
    t = 0
    level = -voltage
    signal.append(level)
    for bit in bits:
        if bit == '1':
            level = voltage if level == -voltage else -voltage
        time.append(t)
        signal.append(level)
        time.append(t + 1)
        signal.append(level)
        t += 1

    plt.plot(time, signal,color='blue')
    plt.title("NRZ-I Encoding")
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.grid(True)
    plt.axhline(0, color='green')
    plt.axvline(0, color='green')
    plt.show()
bits = input("Enter Data Bit: ")
voltage = float(input("Enter Voltage: "))
nrz_i(bits, voltage)