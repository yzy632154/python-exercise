x,y,z=5,6,7
small = x if (x < y and x < z) else (y if y < z else z)
print(small)
