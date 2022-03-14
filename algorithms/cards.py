def recursive(query, cards):
    pt = len(cards) // 2
    if query == cards[pt]:
        return pt
    elif query > cards[pt]:
        return recursive(query, cards[pt:])
    else:
        return recursive(query, cards[:pt])

def linear(query, cards):
    found_it = False
    pt = 0
    for index, card in enumerate(cards):
        if card == query:
            found_it = True
            pt = index
    if found_it:
        return pt
    else:
        return -1

