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
#MODES: 0 - NORMAL SUM / !0 - UNIQUE SUM
def unique_sum(n): 
    def decorator(func):
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = 0
            if (n != 0):
                arrValues =set(args[0])
                
                for number in arrValues:
                    result += number
                return result
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator
        
arr = [ 1, 2, 3, 4, 5, 2, 3, 4 ]
remove_duplicates = unique_sum(1)(sum)
print(remove_duplicates(arr)) 
#MODES: 0 - NORMAL SUM / !0 - UNIQUE SUM