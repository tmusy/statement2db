from statement2db.csvparser import parse


def test_parse():
    result = parse('test.csv')
    print(result)
    assert(0)