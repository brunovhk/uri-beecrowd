"""
Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.

CODE - SPECIFICATION - PRICE
1 - Cachorro-Quente - R$ 4.00
2 - X-Salada        -  R$ 4.50
3 - X-Bacon         - R$ 5.00
4 - Torrada Simples - R$ 2.00
5 - Refrigerante    - R$ 1.50

Input
The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.
"""
N = input().split(' ')
X, Y = N
X = int(X)
Y = int(Y)

if X == 1:
  print(f'Total: R$ {4.00 * Y:.2f}')
if X == 2:
  print(f'Total: R$ {4.50 * Y:.2f}')
if X == 3:
  print(f'Total: R$ {5.00 * Y:.2f}')
if X == 4:
  print(f'Total: R$ {2.00 * Y:.2f}')
if X == 5:
  print(f'Total: R$ {1.50 * Y:.2f}')