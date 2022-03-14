import os

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(locate_card(7, arr))
    #number = 4
    #arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #pointer = len(arr) // 2
    #iterations = 0
    #while arr[pointer] != number:
    #    if number > arr[pointer]:
    #        arr = arr[pointer:]
    #        pointer = len(arr) // 2
    #    else:
    #        arr = arr[:pointer]
    #        pointer = len(arr) // 2
    #    iterations += 1

def locate_card(query, cards):
    pt = len(cards) // 2
    if query == cards[pt]:
        return pt
    elif query > cards[pt]:
        return locate_card(query, cards[pt:])
    else:
        return locate_card(query, cards[:pt])

if __name__=="__main__":
    main()
