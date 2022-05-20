def calculator(n, m, li):
    new_list = []
    z = 0
    x = m
    if n % m == 0:
        number = int(n / m)
    else:
        number = int((n / m) + 1)
    for i in range(int(number)):
        new_list.append(sum(li[z:x]))
        z = x
        x += m
    total = 0
    for ii in range(len(new_list)):
        if ii % 2 == 0:
            total += new_list[ii]
        else:
            total += -(new_list[ii])

    return total
