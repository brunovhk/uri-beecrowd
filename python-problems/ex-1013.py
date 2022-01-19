"""
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:

MaiorAB = (a+b+abs(a-b))/2

Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.
"""
number = input().split(" ")
A, B, C = number
A = int(A)
B = int(B)
C = int(C)

maiorAB = (A+B+abs(A-B))/2
maiorABC = (maiorAB + C + abs(maiorAB-C))/2
maiorABC = int(maiorABC)

print(f'{maiorABC} eh o maior')