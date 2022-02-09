"""
Write an algorithm that reads two floating values (x and y), which should represent the coordinates of a point in a plane. Next, determine which quadrant the point belongs, or if you are at one of the Cartesian axes or the origin (x = y = 0).



If the point is at the origin, write the message "Origem".

If the point is at X axis write "Eixo X", else if the point is at Y axis write "Eixo Y".

Input
The input contains the coordinates of a point.

Output
The output should display the quadrant in which the point is.
"""
point = input().split()
x, y = point

x = float(x)
y = float(y)

if x == 0:
  if y == 0:
    print('Origem')
  elif y != 0:
    print('Eixo Y')
if y == 0:
  if x != 0:
    print('Eixo X')

if x > 0:
  if y > 0:
    print('Q1')
  if y < 0:
    print('Q4')
if x < 0:
  if y > 0:
    print('Q2')
  if y < 0:
    print('Q3')