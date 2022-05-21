def base(decimal, basee):
    list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    other_base = ""
    while decimal != 0:
        x = decimal % basee
        # print("x", type(x))
        other_base = list[x] + other_base
        decimal = int(decimal / basee)
    if other_base == "":
        other_base = "0"
    return other_base


def is_symmetrical_num(n):
    return str(n) == str(n)[::-1]


x = int(input())
for i in range(1, 300):
    number = base(i ** 2, x)
    if is_symmetrical_num(number):
        print(base(i, x), number)

