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
result = None
seen = {}

for index, num in enumerate(m):
    subtraction = z - num
    if subtraction in seen:
        result = seen[subtraction], index
        break 
    seen[num] = index

if result :
    i, j = result
    print(f"m[{i}] + m[{j}] = {m[i]} + {m[j]} = {z}")
else: 
    print("No pair found")


    


