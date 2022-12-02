"""
Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
"""

banknote = float(input())
n100 = banknote // 100
banknote = banknote - n100 * 100

n50 = banknote // 50
banknote = banknote - n50 * 50

n20 = banknote // 20
banknote = banknote - n20 * 20

n10 = banknote // 10
banknote = banknote - n10 * 10

n5 = banknote // 5
banknote = banknote - n5 * 5

n2 = banknote // 2
banknote = banknote - n2 * 2

m1 = banknote // 1
banknote = banknote - m1 * 1

m050 = banknote // 0.50
banknote = banknote - m050 * 0.50 + 0.00001

m025 = banknote // 0.25
banknote = banknote - m025 * 0.25

m010 = banknote // 0.10
banknote = banknote - m010 * 0.10

m005 = banknote // 0.05
banknote = banknote - m005 * 0.05

m001 = banknote // 0.01
banknote = banknote - m001 * 0.01

print('NOTAS:')
print(f'{n100:.0f} nota(s) de R$ 100.00')
print(f'{n50:.0f} nota(s) de R$ 50.00')
print(f'{n20:.0f} nota(s) de R$ 20.00')
print(f'{n10:.0f} nota(s) de R$ 10.00')
print(f'{n5:.0f} nota(s) de R$ 5.00')
print(f'{n2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{m1:.0f} moeda(s) de R$ 1.00')
print(f'{m050:.0f} moeda(s) de R$ 0.50')
print(f'{m025:.0f} moeda(s) de R$ 0.25')
print(f'{m010:.0f} moeda(s) de R$ 0.10')
print(f'{m005:.0f} moeda(s) de R$ 0.05')
print(f'{m001:.0f} moeda(s) de R$ 0.01')

