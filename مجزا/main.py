def separator(ls):
    even_t=list()
    odd_t=list()

    for i in ls:
        if i%2==0:
            even_t.append(i)
        if i%2!=0:
            odd_t.append(i)

    t=even_t,odd_t

    return (t)

separator([-3, -2, -1, 0, 1, 2, 3])
