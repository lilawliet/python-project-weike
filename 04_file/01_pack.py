import struct

a = 'hello'
b = 'world!'
c = 2
d = 45.123
e = 20

bytes = struct.pack('5s6sif', a.encode('utf-8'), b.encode('utf-8'), c, d)

# bytes = struct.pack('b', 20)

print(bytes)
print(struct.unpack('5s6sif', bytes))