def soma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def soma2(args:list):
    if len(args) == 1:
        return args[0]
    else:
        return args[0] + soma2(args[1:])
    
print(soma(1, 2, 3, 4, 5))

print(soma2([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5]))