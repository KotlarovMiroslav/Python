dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
# Резултат:
#Solution 1 based on today's lesson 31/08/2026
res = {**dict_a, **dict_b, **dict_c}
print(f"Result 1: {res}")
#Solution 2 based on previous lecture
res2 =  dict_a | dict_b | dict_c
print(f"Result 2: {res2}")