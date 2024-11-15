a = "11.10.2024	B	SZ0319"

print(a)

b = a.split('.')[0]
c = a.split('.')[1]
d = a.split('.')[2]

print(b)
print(c)
print(d)

e = b + '.' + c + ' ' + d

print(e)
