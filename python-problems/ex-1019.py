"""
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
"""
N = int(input())
hours = N // 3600
N = N - hours * 3600
minutes = N // 60
N = N - minutes * 60
seconds = N
print(f'{hours}:{minutes}:{seconds}')
