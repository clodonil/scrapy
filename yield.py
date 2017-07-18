def lista():
    l=[10,20,30]
    for x in l:
       yield x


g = lista()
print(next(g))
print(next(g))
print(next(g))
