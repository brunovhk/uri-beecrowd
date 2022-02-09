"""
Read three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

Input
The input contains three integer numbers.

Output
Present the output as requested above.
"""
list = input().split()
a, b, c = list
list[0] = int(a)
list[1] = int(b)
list[2] = int(c)
list2 = list.copy()
list.sort()
print(list[0])
print(list[1])
print(list[2])
print("")
print(list2[0])
print(list2[1])
print(list2[2])