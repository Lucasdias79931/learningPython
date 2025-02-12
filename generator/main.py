iterable = ['eu', 'tenho', '__inter__']
iterator = iter(iterable)

generator = (n for n in range(100))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
