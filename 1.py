with open('function-defect.txt', 'r') as f:
    fun = f.readlines()
functions = [''.join(x[1:47].split(', ')) for x in fun]
# print(functions[:10])

with open('results_4.txt', 'r') as f:
    functionsmy = f.readlines()
functionsmy = [x[:-1] for x in functionsmy]
# functionsmy.append('1111111111111111')
# print(functionsmy[:10])

s1 = set(functions)
print(len(s1))

s2 = set(functionsmy)
print(len(s2))

# print(len(s1 & s2))

print((s1 ^ (s1 & s2)))


# ----------------
def dnf(a):
    if a[0] == '1':
        print('not x1 and not x2 and not x3 and not x4')
    if a[1] == '1':
        print('not x1 and not x2 and not x3 and x4')
    if a[2] == '1':
        print('not x1 and not x2 and x3 and not x4')
    if a[3] == '1':
        print('not x1 and not x2 and x3 and x4')
    if a[4] == '1':
        print('not x1 and x2 and not x3 and not x4')
    if a[5] == '1':
        print('not x1 and x2 and not x3 and x4')
    if a[6] == '1':
        print('not x1 and x2 and x3 and not x4')
    if a[7] == '1':
        print('not x1 and x2 and x3 and x4')
    if a[8] == '1':
        print('x1 and not x2 and not x3 and not x4')
    if a[9] == '1':
        print('x1 and not x2 and not x3 and x4')
    if a[10] == '1':
        print('x1 and not x2 and x3 and not x4')
    if a[11] == '1':
        print('x1 and not x2 and x3 and x4')
    if a[12] == '1':
        print('x1 and x2 and not x3 and not x4')
    if a[13] == '1':
        print('x1 and x2 and not x3 and x4')
    if a[14] == '1':
        print('x1 and x2 and x3 and not x4')
    if a[15] == '1':
        print('x1 and x2 and x3 and x4')


# ---------------

# print((list(s1 ^ (s1 & s2)))[0])

for i in range(len(s1 ^ (s1 & s2))):
    print(i+1,'-----------')
    print((list(s1 ^ (s1 & s2)))[i])
    dnf((list(s1 ^ (s1 & s2)))[i])
