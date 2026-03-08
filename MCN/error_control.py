# Parity Method
data = input("Enter binary data: ")
ones = data.count('1')
if ones % 2 == 0:
    parity = '0'
else:
    parity = '1'
transmitted = data + parity
print("Data with Even Parity:", transmitted)

# Block Parity Method
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter binary rows:")
for i in range(rows):
    row = list(input())
    matrix.append(row)

for row in matrix:
    parity = str(row.count('1') % 2)
    row.append(parity)

col_parity = []
for j in range(cols + 1):
    count = 0
    for i in range(rows):
        if matrix[i][j] == '1':
            count += 1
    col_parity.append(str(count % 2))

matrix.append(col_parity)
print("Block Parity Frame:")
for r in matrix:
    print(" ".join(r))

# CRC
def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

def crc(data, key):
    l_key = len(key)
    appended = data + '0'*(l_key-1)
    temp = appended[0:l_key]
    while l_key < len(appended):
        if temp[0] == '1':
            temp = xor(key, temp) + appended[l_key]
        else:
            temp = xor('0'*l_key, temp) + appended[l_key]
        l_key += 1
    if temp[0] == '1':
        temp = xor(key, temp)
    else:
        temp = xor('0'*len(key), temp)
    remainder = temp
    return data + remainder

data = input("Enter data: ")
key = input("Enter generator polynomial: ")
codeword = crc(data, key)
print("CRC Codeword:", codeword)

# Checksum
def checksum(data):
    total = 0
    for block in data:
        total += int(block, 2)
    checksum = bin(~total & 0xFF)[2:]
    return checksum

n = int(input("Enter number of blocks: "))
blocks = []
for i in range(n):
    blocks.append(input("Enter block: "))
cs = checksum(blocks)
print("Checksum:", cs)

# Hamming Code
data = input("Enter binary data: ")
m = len(data)
r = 0
while (2**r) < (m + r + 1):
    r += 1
arr = ['0'] * (m + r)
j = 0
for i in range(1, m + r + 1):
    if (i & (i-1)) != 0:
        arr[i-1] = data[j]
        j += 1

for i in range(r):
    pos = 2**i
    parity = 0
    for j in range(1, m + r + 1):
        if j & pos:
            parity ^= int(arr[j-1])
    arr[pos-1] = str(parity)
print("Hamming Code:", "".join(arr))

# Reed Solomon Code
import reedsolo
data = input("Enter message: ").encode()
rs = reedsolo.RSCodec(10)   # 10 parity symbols
encoded = rs.encode(data)
print("Encoded Data:", encoded)
decoded = rs.decode(encoded)
print("Decoded Data:", decoded[0].decode())