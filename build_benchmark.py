from build_pycompat import tests

def main():
    test_strings = []

    for _, strings in tests.items():
        test_strings.extend(strings)

    header = '''#![feature(test)]
extern crate test;
extern crate dtparse;

use test::Bencher;
use dtparse::parse;

#[bench]
fn test_strings(b: &mut Bencher) {\n    b.iter(|| {\n        '''

    body = ';\n        '.join(['parse("{}").unwrap()'.format(x) for x in test_strings])
    footer = ';\n    });\n}'

    with open('benches/test_suite.rs', 'w+') as handle:
        handle.write(header)
        handle.write(body)
        handle.write(footer)

if __name__ == '__main__':
    main()