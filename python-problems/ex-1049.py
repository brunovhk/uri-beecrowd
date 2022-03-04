"""
In this problem, your job is to read three Portuguese words. These words define an animal according to the table below, from left to right. After, print the chosen animal defined by these three words.

Vertebrado -> ave -> carnivoro -> aguia
                    -> onivoro -> pomba
          -> mamifero -> onivoro -> homem
                      -> herbivoro -> vaca

invertebrado -> inseto -> hematofago -> pulga
                    -> herbivoro -> lagarta
             -> anelideo -> hematofago -> sanguessuga
                           -> onivoro -> minhoca

Input
The input contains 3 words, one by line, that will be used to identify the animal, according to the above table, with all letters in lowercase.

Output
Print the animal name according to the given input.
"""
l1 = input()
l2 = input()
l3 = input()

if l1 == 'vertebrado' and l2 == 'ave' and l3 == 'carnivoro':
    animal = 'aguia'

if l1 == 'vertebrado' and l2 == 'ave' and l3 == 'onivoro':
    animal = 'pomba'

if l1 == 'vertebrado' and l2 == 'mamifero' and l3 == 'onivoro':
    animal = 'homem'

if l1 == 'vertebrado' and l2 == 'mamifero' and l3 == 'herbivoro':
    animal = 'vaca'

if l1 == 'invertebrado' and l2 == 'inseto' and l3 == 'hematofago':
    animal = 'pulga'

if l1 == 'invertebrado' and l2 == 'inseto' and l3 == 'herbivoro':
    animal = 'lagarta'

if l1 == 'invertebrado' and l2 == 'anelideo' and l3 == 'hematofago':
    animal = 'sanguessuga'

if l1 == 'invertebrado' and l2 == 'anelideo' and l3 == 'onivoro':
    animal = 'minhoca'

print(animal)
