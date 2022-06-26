card_tests = []

card_tests.append({
    'name': "Cards Test",
    'description': "When query occurs in the middle",
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

card_tests.append({
    'name': "Cards Test",
    'description': "When query is the first element",
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

card_tests.append({
    'name': "Cards Test",
    'description': "When the query is the last element",
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

card_tests.append({
    'name': "Cards Test",
    'description': "When the cards contains just one element",
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

card_tests.append({
    'name': "Cards Test",
    'description': "When the cards not contains the query",
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})


algo_tests = []

algo_tests.append({
    'description': "sample",
    'input': {
        'cards': ['s', 'a', 'm', 'p', 'l', 'e'],
        'query': 's'
    },
    'output': 0
})
