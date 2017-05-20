import random as random_number

N = 500000
M = 0
for dummy_j in range(N):
    six = 0
    r1 = random_number.randint(1, 6)
    if r1 == 6:
        six += 1
    r2 = random_number.randint(1, 6)
    if r2 == 6:
        six += 1
    r3 = random_number.randint(1, 6)
    if r3 == 6:
        six += 1
    r4 = random_number.randint(1, 6)
    if r4 == 6:
        six += 1
    if six >= 2:
        M += 1

p = float(M)/N
print('probability:', p)

import sys

ndice = 4
nsix = 2
M = 0
for dummy_i in range(N):
    six =0
    for j in range(ndice):
        r = random_number.randint(1, 6)
        if r == 6:
            six += 1
    if six >= nsix:
        M += 1

pp = float(M)/N
print('Probability:', pp)

import numpy

eyes = random.random_integers(1, 6, (N, ndice))
compare = eyes == 6
nthrows_with_6 = sum(compare, axis=1)  # суммирование по столбцам - элементам строки (axis = 1)
nsuccesses = nthrows_with_6 >= nsix
M = sum(nsuccesses)
ppp = float(M)/N
print('probability:', ppp)
