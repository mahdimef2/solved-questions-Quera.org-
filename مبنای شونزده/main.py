x = input()

base10 = int(x, 16)

base10 += 1

base16 = hex(base10)

print(base16[2:].upper())
