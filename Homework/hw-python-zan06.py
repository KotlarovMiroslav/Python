def sum(m):
    if(len(m) == 0):
        return 0
    elif(type(m[0]) == list):
        return sum(m[0]) + sum(m[1:])
    else:
        return m[0] + sum(m[1:])
    

m = [1,2,3, [ 5,6, [ 7 ] ], 4]


print(sum(m))

