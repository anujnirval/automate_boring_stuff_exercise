def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid Arguement.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


def spa(divideBy):
    return 42 / divideBy

try:
    print(spa(2))
    print(spa(12))
    print(spa(0))
    print(spa(1))
except ZeroDivisionError:
    print('Error: Invalid Arguement.')
