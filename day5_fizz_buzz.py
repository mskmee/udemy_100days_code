total = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        i = 'FizzBuzz'
    elif i % 5 == 0:
        i = 'buzz'
    elif i % 3 == 0:
        i = 'fizz'
    print(i)