#Зад. 7
from functools import wraps

def toString(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        genValues = func(*args, **kwargs)
        
        for number in genValues:
            yield str(number)
    return wrapper
    
@toString
def getNumbers(n):
    numbers = []
    while n > 0:
        numbers.append(n % 10)
        n = int(n / 10)
    numbers.reverse()
    for i in numbers:
        yield i

for i in getNumbers(123):
    print(f"{i} and type: {type(i)}")

#Зад. 8

def remove_duplicates(func):
    @wraps(func)
    def wrapper(*args):
            wrapper.original = func
            arrValues = set(args[0])
            return func(arrValues)
    return wrapper

        
arr = [ 1, 2, 3, 4, 5, 2, 3, 4 ]
print(sum(arr))
sum = remove_duplicates(sum)
print(sum(arr))
sum = sum.original
print(sum(arr))
