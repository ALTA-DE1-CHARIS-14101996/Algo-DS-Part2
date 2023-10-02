def playing_domino(cards, deck):
    accum = []
    for i in cards:
        if i[0] in deck or i[1] in deck:
            accum.append(i)
    if accum == []:
        return []
    else:
        result = max(accum)              
    return result

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []