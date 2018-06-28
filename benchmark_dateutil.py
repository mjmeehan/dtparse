from timeit import timeit
from dateutil.parser import parse

from build_pycompat import tests

def main():
    iter = 1000
    test_strings = []

    for _, strings in tests.items():
        test_strings.extend(strings)

    def parse_test():
        for s in test_strings:
            parse(s)

    res = timeit('parse_test()', number=iter, globals={'parse_test': parse_test})

    print('Ran through {} iterations in {} seconds, {:.3f}ms average'.format(
        iter, res, res / iter * 1000
    ))

if __name__ == '__main__':
    main()
