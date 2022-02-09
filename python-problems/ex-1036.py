"""
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
"""
import math

inputFloat = input()
list = inputFloat.split(' ')
A, B, C = list
A = float(A)
B = float(B)
C = float(C)

delta = ((B ** 2) - (4 * A * C))

if A == 0 or delta < 0:
  print('Impossivel calcular')
else:
  delta = math.sqrt(delta)
  x1 = ((-B + delta) / (2 * A))
  x2 = ((-B - delta) / (2 * A))
  print(f'R1 = {x1:.5f}')
  print(f'R2 = {x2:.5f}')