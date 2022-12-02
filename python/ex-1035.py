"""
Read 4 integer values A, B, C and D. Then if B is greater than C and D is greater than A and if the sum of C and D is greater than the sum of A and B and if C and D were positives values and if A is even, write the message “Valores aceitos” (Accepted values). Otherwise, write the message “Valores nao aceitos” (Values not accepted).

Input
Four integer numbers A, B, C and D.

Output
Show the corresponding message after the validation of the values​​.
"""
inputInt = input()
list = inputInt.split(' ')
A, B, C, D = list
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if (B > C) and (D > A) and (((C + D) > (A + B))) and ((C + D) > 0):
  print('Valores aceitos')
else:
  print('Valores nao aceitos')