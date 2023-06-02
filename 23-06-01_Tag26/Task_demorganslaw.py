def de_morgans_laws1(p,q):
    return not (p or q)

def de_morgans_laws2(p,q):
    return (not p) and (not q)

def de_morgans_laws3(p,q):
    return not (p and q)

def de_morgans_laws4(p,q):
    return (not p) or (not q)



p = True
q = True
print(de_morgans_laws1(p,q))
print(de_morgans_laws2(p,q))
print(de_morgans_laws3(p,q))
print(de_morgans_laws4(p,q))
