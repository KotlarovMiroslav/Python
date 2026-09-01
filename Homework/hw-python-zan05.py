# Решението е в O(n) сложност, но не покрива ситуацията в която
# ако се промени големината на масива.
# (Решението покрива масив с големина от 6 елемента само). 
# Реално погледнато решението на задачата може да има доста различни
# варианта. 
# Мога да се пробвам да я пререша но не успявам да се сетя подходящ 
# подход спрямо условието на задачата.
# В това решение съм използвал допълнителен масив - копие на оригинала.
print("Introduction:\n" \
"Input a whole number and the program will check if the sum of two of the numbers in the following array:\n" \
"[1,4,6,8,9,23]\n" \
"is equal to the sum of the number you have entered\n\n")
z = int(input("Enter a whole number:"))
m = [1,4,6,8,9,23]
m2 = m

for i in range(0, len(m)):
    i0 = m[0] + m2[(1+i) % len(m)]
    i1 = m[1] + m2[(2+i) % len(m)]
    i2 = m[2] + m2[(3+i) % len(m)]
    i3 = m[3] + m2[(4+i) % len(m)]
    i4 = m[4] + m2[(5+i) % len(m)]
    i5 = m[5] + m2[(6+i) % len(m)]

    if(z == i0 or z == i1 or z == i2 or z == i3 or z == i4 or z == i5):
        print("A solution has been found!\n\n\n\n")
        break




if(i0 == z):
    print(f"Solution: {m[0]} + {m2[(0+i) % len(m)]}")
    pass
elif(i1 == z):
    print(f"Solution: {m[1]} + {m2[(1+i) % len(m)]}")
    pass
elif(i2 == z):
    print(f"Solution: {m[2]} + {m2[(2+i) % len(m)]}")
    pass
elif(i3 == z):
    print(f"Solution: {m[3]} + {m2[(3+i) % len(m)]}")
    pass
elif(i4 == z):
    print(f"Solution: {m[4]} + {m2[(4+i) % len(m)]}")
    pass
elif(i5 == z):
    print(f"Solution: {m[5]} + {m2[(5+i) % len(m)]}")
    pass
   

    


