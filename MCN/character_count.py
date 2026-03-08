# Bit Count Method
data = input("Enter data: ")
count = len(data)
frame = str(count) + data
print("Frame after Bit Count Method:", frame)

# Byte Stuffing Method
data = input("Enter data: ")
FLAG = "Flag"
ESC = "ESC"
stuffed = ""
for ch in data:
    if ch == FLAG or ch == ESC:
        stuffed += ESC
    stuffed += ch
frame = FLAG + stuffed + FLAG
print("Frame after Byte Stuffing:", frame)

# Bit Stuffing Method
data = input("Enter binary data: ")
count = 0
stuffed = ""
for bit in data:
    stuffed += bit
    if bit == '1':
        count += 1
    else:
        count = 0
    if count == 5:
        stuffed += '0'
        count = 0
print("Data after Bit Stuffing:", stuffed)

# Physical Layer Coding Violation
data = input("Enter binary data: ")
START = "V"
END = "V"
frame = START + data + END
print("Frame using Physical Layer Violation:", frame)