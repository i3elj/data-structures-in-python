def tester():
    index = 0
    while index < len(tst):
        result = linear(tst[index]['input']['query'], tst[index]['input']['cards'])
        print(f"Test {index}: {result == tst[index]['output']}")
        index += 1
