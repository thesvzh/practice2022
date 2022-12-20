def f_0(x1, x2):
    return 0


def f_1(x1, x2):
    return 1


def f_2(x1, x2):
    return x1


def f_3(x1, x2):
    return x2


def f_4(x1, x2):
    return int(not x1)


def f_5(x1, x2):
    return int(not x2)


def f_6(x1, x2):
    return int(not x1 and not x2)


def f_7(x1, x2):
    return int(x1 and x2)


def f_8(x1, x2):
    return int(x1 or not x2)


def f_9(x1, x2):
    return int(not x1 or x2)


def f_10(x1, x2):
    return int((x1 and x2) or (not x1 and not x2))


def f_11(x1, x2):
    return int(x1 and not x2)


def f_12(x1, x2):
    return int(not x1 and x2)


def f_13(x1, x2):
    return int(not x1 or not x2)


def f_14(x1, x2):
    return int(x1 or x2)


def f_15(x1, x2):
    return int((not x1 and x2) or (x1 and not x2))


mn_dif = set()
v = []

bool = [0, 1]

# f_0
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_1
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))
# print (zz)

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_2
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_3

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_4
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_5

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_6
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_6(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_7
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_7(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_8
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_8(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_9
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_9(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# f_10
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_11(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_12(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_13(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_14(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_10(x1, x2) and f_15(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn_dif.add(int(zz, 2))

# ------------

mn = set()
v = []

# f_0
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_0(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
                mn.add(int(zz, 2))

# f_1

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))
# print (zz)

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_1(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

# f_2

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_2(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

# f_3

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_3(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

# f_4
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_4(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

# f_5

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_5(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

# f_11
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_11(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

# f_12
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_12(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

# f_13
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_13(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

# f_14
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_14(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

# f_15
v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_0(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_1(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_2(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_3(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_4(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_5(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_6(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_7(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_8(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_9(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

v = []
for x1 in bool:
    for x2 in bool:
        for x3 in bool:
            for x4 in bool:
                v.append(int(f_15(x1, x2) and f_10(x3, x4)))
                zz = ''.join([str(i) for i in v])
mn.add(int(zz, 2))

print(len(mn))
print(len(mn_dif))
ls = list(mn)
ls_dif = list(mn_dif)
# print(len(ls), " ", len(ls_dif))

mn_finale = set()

for i in range(len(ls)):
    for j in range(len(ls_dif)):
        mn_finale.add(ls[i] | ls_dif[j])

print(len(mn_finale))

z = list(mn_finale)
z.sort()

with open("results_4.txt", "w") as f:
    f.write("\n".join([bin(i)[2:].rjust(16, '0') for i in z]))
f.close()

# print(4723 - len(mn_finale))
# with open("results_4_10.txt", "w") as f:
#    f.write("\n".join([bin(i)[2:].rjust(16,'0') for i in z]))
# f.close()
