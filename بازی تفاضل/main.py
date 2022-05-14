def game(number):
    number=int(number)
    first=number%10
    second=int(number/10)
    return(abs(first-second))

print(game(23))
