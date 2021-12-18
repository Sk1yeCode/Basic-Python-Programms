# Fizzbuzz in Python

for i in range(1, 101):
    if (i % 3):
        if (i % 5):
            print('FizzBuzz')
        else:
            print('Fizz')
    elif (i % 5):
        print('Buzz')
        
