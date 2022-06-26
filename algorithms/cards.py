def recursive(query: int, cards: list[int]) -> int:
    pt: list[int] = len(cards) // 2
    if query == cards[pt]:
        return pt
    elif query > cards[pt]:
        return recursive(query, cards[pt:])
    else:
        return recursive(query, cards[:pt])


def linear(query: int, cards: list[int]) -> int:
    found_it: bool = False
    pt: int = 0
    for index, card in enumerate(cards):
        if card == query:
            found_it = True
            pt = index
    if found_it:
        return pt
    else:
        return -1
