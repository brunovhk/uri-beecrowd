"""
Read three point floating values (A, B and C) and verify if is possible to make a triangle with them. If it is possible, calculate the perimeter of the triangle and print the message:


Perimetro = XX.X


If it is not possible, calculate the area of the trapezium which basis A and B and C as height, and print the message:


Area = XX.X

Input
The input file has tree floating point numbers.

Output
Print the result with one digit after the decimal point.
"""
list = input().split()
a, b, c = list
a = float(list[0])
b = float(list[1])
c = float(list[2])

if (a + b) > c and (a + c) > b and (b + c) > a:
  P = a + b + c
  print(f'Perimetro = {P:.1f}')
else:
  area = ((a + b) * c )/ 2
  print(f'Area = {area:.1f}')