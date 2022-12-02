"""
Read the start time and end time of a game, in hours and minutes (initial hour, initial minute, final hour, final minute). Then print the duration of the game, knowing that the game can begin in a day and finish in another day,

Obs.: With a maximum game time of 24 hours and the minimum game time of 1 minute.

Input
Four integer numbers representing the start and end time of the game.

Output
Print the duration of the game in hours and minutes, in this format: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” . Which means: the game lasted XXX hour(s) and YYY minutes.
"""
ihour, iminute, fhour, fminute = list(map(int, input().split()))

iminute += ihour * 60
fminute += fhour * 60

gametime = fminute - iminute
if gametime <= 0:
    gametime += 24 * 60

ghour = gametime // 60
gminute = gametime % 60

print(f'O JOGO DUROU {ghour} HORA(S) E {gminute} MINUTO(S)')
