#!/usr/bin/env python3


z, y, x = 2, 1, 0
x, z = z, y
# x = 2 and z = 1
y = y - z
# y = 0

# put line here

x, y, z = y, z, x   # This line or
z, y, x = x, z, y   # that


print(x, y, z)
