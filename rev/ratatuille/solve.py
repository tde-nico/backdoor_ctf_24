flag = [120, 33, 56, 85, 25, 121, 17, 114, 122, 35, 111, 31, 91, 57, 78, 52, 105, 100, 113, 75]
items = [8, 16, 66, 47, 45, 10, 60, 70]

for i in range(len(flag)):
	flag[i] ^= items[i % len(items)]

print(f'flag{{{bytes(flag).decode()}}}')

# flag{p1zz4s-4r3-0v3rrat3d}
