"""
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).

Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.
"""
banknote = int(input())
print(banknote)
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

n1 = banknote // 1
banknote = banknote - n1 * 1


print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')