import matplotlib.pyplot as plt
def rz_unipolar(bits, voltage):
    time = [0]
    signal = [0]
    t = 0
    for bit in bits:
      if bit == '1':
        time.append(t)
        signal.append(voltage)
        time.extend([t, t + 0.5])
        signal.extend([voltage, voltage])
        time.extend([t + 0.5, t + 1])
        signal.extend([0, 0])
      else:
        time.append(t)
        signal.append(0)
        time.extend([t, t + 1])
        signal.extend([0, 0])
      t += 1
    plt.plot(time, signal,color='black')
    plt.title("RZ Unipolar Encoding")
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    plt.grid(True)
    plt.axhline(0, color='green')
    plt.axvline(0, color='green')
    plt.show()
bits = input("Enter Data Bit: ")
voltage = float(input("Enter Voltage: "))
rz_unipolar(bits, voltage)