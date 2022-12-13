import math


def get_input():
    lines = []
    with open("input.txt","r") as input_txt:
        lines=[line.rstrip() for line in input_txt.readlines() if line != "\n"]
    return lines


def rps(m,n):
    if abs(m-n) <=1:
        return m-n
    else:
        return m-n-math.copysign(3,m-n)


def score_round(their_shape, your_shape):
    result = rps(m,n)
    if result == -1:
        return m + 0, n + 6
    elif result == 1:
        return m + 6, n + 0
    else:
        return m + 3, n + 3

shapes = { 'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3 }
    
their_total = 0 
your_total = 0
for line in get_input():
    their_shape, your_shape = line.split(" ")
    m = shapes[their_shape]
    n = shapes[your_shape]
    their_score, your_score = score_round(m,n)
    your_total = your_total + your_score
    their_total = their_total + their_score

print(their_total,your_total)
    
shapes = { 'A': 1, 'B': 2, 'C': 3 }

their_total = 0 
your_total = 0
for line in get_input():
    their_shape, your_shape = line.split(" ")
    m = shapes[their_shape]
    if your_shape == 'X':
        n = m - 1
        if n == 0:
            n = 3
    elif your_shape == 'Z':
        n = m + 1
        if n == 4:
            n = 1
    else:
        n = m
    print(their_shape,your_shape,m,n)
    their_score, your_score = score_round(m,n)
    your_total = your_total + your_score
    their_total = their_total + their_score

print(their_total,your_total)
