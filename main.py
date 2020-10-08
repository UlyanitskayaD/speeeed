def odometer(z, g):
	if len(z) < g:
		z = '0' * (g - len(z)) + z
	y = ''
	for i in range(len(z)):
		y = z[i] + y
	return int(y)


print(odometer('1', 5))
print(odometer('1000', 6))
print(odometer('1000', 9))

for a in range(10):
	for b in range(10):
		for c in range(10):
			for d in range(10):
				for e in range(10):
					for f in range(10):
						x = int(str(a) + str(b) + str(c) + str(d) + str(e) + str(f))
						if odometer(str(x % 10000), 5) == x % 10000:
							if odometer(str((x + 1) % 10000), 5) == (x + 1) % 10000:
								if odometer(str((x + 2) % 10000 // 10), 5) == (x + 2) % 10000 // 10:
									if odometer(str((x + 3)), 5) == (x + 3):
										print(a, b, c, d, e, f, sep='')
