import random
def random_line(hello.txt):
    lines = open(hello.txt).read().splitlines()
    return random.choice(lines)
print(random_line('C:/PYTHON/Module-3/hello.txt'))
