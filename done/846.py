from collections import Counter

hand = [8,10,12]
size = 3

def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False

    card_count = {}
    for card in hand:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1

    sorted_cards = sorted(card_count)

    for card in sorted_cards:
        while card in card_count and card_count[card] > 0:
            for i in range(groupSize):
                current_card = card + i
                if current_card not in card_count or card_count[current_card] <= 0:
                    return False
                card_count[current_card] -= 1
                if card_count[current_card] == 0:
                    del card_count[current_card]

    return True

print(isNStraightHand(hand,size))