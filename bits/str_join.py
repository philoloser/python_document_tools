xs = ['1', '2', '3']

loop = 1
looplist = []

for i in xs:
    lp = loop.__str__() + '. ' + i
    print(lp)
    looplist.append(loop)
    loop = loop + 1

print(looplist)

# s = '_'.join(xs)
# print(s)
