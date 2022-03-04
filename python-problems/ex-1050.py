"""
Read an integer number that is the code number for phone dialing. Then, print the destination according to the following table:




If the input number isn’t found in the above table, the output must be:
DDD nao cadastrado
That means “DDD not found” in Portuguese language.

Input
The input consists in a unique integer number.

Output
Print the city name corresponding to the input DDD. Print DDD nao cadastrado if doesn't exist corresponding DDD to the typed number.
"""
codeNumber = int(input())

brasilia = 61
salvador = 71
sp = 11
rj = 21
juizdefora = 32
campinas = 19
vitoria = 27
bh = 31

if codeNumber == brasilia:
    print('Brasilia')
elif codeNumber == 71:
    print('Salvador')
elif codeNumber == 11:
    print('Sao Paulo')
elif codeNumber == 21:
    print('Rio de Janeiro')
elif codeNumber == 32:
    print('Juiz de Fora')
elif codeNumber == 19:
    print('Campinas')
elif codeNumber == 27:
    print('Vitoria')
elif codeNumber == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')
