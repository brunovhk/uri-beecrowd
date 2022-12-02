"""
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

Input
The input file contains three double values with one digit after the decimal point.

Output
The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be presented with 3 digits after the decimal point.
"""
area = input().split(" ")
A, B, C = area
A = float(A)
B = float(B)
C = float(C)

rectangle_t = A * C / 2
circle = C ** 2 * 3.14159
trapezium = (A + B) / 2 * C
square = B ** 2
rectangle = A * B

print(f'TRIANGULO: {rectangle_t:.3f}')
print(f'CIRCULO: {circle:.3f}')
print(f'TRAPEZIO: {trapezium:.3f}')
print(f'QUADRADO: {square:.3f}')
print(f'RETANGULO: {rectangle:.3f}')