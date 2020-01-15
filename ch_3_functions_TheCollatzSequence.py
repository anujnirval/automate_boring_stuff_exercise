def collatz(number):

    if number % 2 == 0:
        result = number // 2
        print(result);
        return result

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
try:
    print('Enter a number: ')
    enter = int(input())
except ValueError:
    print("Please enter a valid INTEGER.")
response = 0
while enter!= 1:
    enter  = collatz(enter)
