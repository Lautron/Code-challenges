values = 'A23456789TJQK'
types = 'cdhs'

def encode(cards):
    return [values.index(card[0]) + types.index(card[1]) * 13 for card in cards]
def decode(cards):
    return [values[card % 13] + types[card // 13] for card in cards]
