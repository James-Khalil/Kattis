from bitarray import bitarray

# Create bitarrays of size 8
bit_array1 = bitarray(8)
bit_array2 = bitarray(8)
n = int(input())
numbers = [n]
line = input().split()
for _ in range(n):
    number = int(line[_])
    temp = (bytes([number]))
    temp1 = (bytes([number << 1]))[:8]
    bit_array1.frombytes(bytes([number]))
    bit_array2 = (bit_array1 << 1)[:8]

    result = bit_array1 ^ bit_array2
    print(int(result.to01(), 2))
