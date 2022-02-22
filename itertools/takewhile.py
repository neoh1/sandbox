from itertools import takewhile

def match_iter(self, other):
    return sum(1 for x in takewhile(lambda x: x[0] == x[1],
                                        zip(self, other)))

def match_loop(self, other):
    element = -1
    for element in range(min(len(self), len(other))):
        if self[element] != other[element]:
            element -= 1
            break
    return element +1

def test():
    a = [0, 1, 2, 3, 4, 5]
    b = [0, 1, 2, 3, 4, 5, 6, 0]

    print(f"match_loop a={a}, b={b}, result={match_loop(a,b)}")
    print(f"match_iter a={a}, b={b}, result={match_iter(a,b)}")

    i=0
    while i < 10000:
        match_loop(a, b)
        match_iter(a, b)
        i += 1

def profile_test():
    import cProfile
    cProfile.run('test()')

if __name__ == '__main__':
    profile_test()
