import matplotlib.pyplot as plt
def nrz_l(bits, voltage):
    time = [0]
    signal = []
    first_level = voltage if bits[0] == '1' else -voltage
    signal.append(first_level)
    t = 0
    for bit in bits:
        level = voltage if bit == '1' else -voltage
        time.append(t)
        signal.append(level)
        time.append(t + 1)
        signal.append(level)
        t += 1

    plt.plot(time, signal,color='blue')
    plt.title("NRZ-L Encoding")
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.grid(True)
    plt.axhline(0, color='green')
    plt.axvline(0, color='green')
    plt.show()

bits = input("Enter Data Bit: ")
voltage = float(input("Enter Voltage: "))
nrz_l(bits,voltage)