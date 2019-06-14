def perm(elems):
    for i in recursive_perm(elems,[]):
        print(perm)
def recursive_perm(elems,sofar):
    if len(elems)==0:
        yield sofar
    else:
        for i in range(0,len(elems)):
            for j in recursive_perm(elems[0:i]+elems[i+1:],sofar+[elems[i]]):
                yield j
print(recursive_perm("ABC",""))