e = 0.0001

def wb(x):
    if x < 0: return -x;
    else: return x;

p = 9
a1 = 1
a2 = p
while wb(a1 - a2) > e:
    a1 = (a1+a2)/2
    a2 = p/a1