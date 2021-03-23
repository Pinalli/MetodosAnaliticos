def seedLCG(valInit):
    global rand
    rand = valInit

def lcg():
    a = 33
    c = 11
    m = 2 ** 31
    global rand
    rand = (a * rand + c) % m
    return rand / m

seedLCG(13)

for i in range(1000):
    print('%.4f'%(lcg()))