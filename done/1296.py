## Cf exo 846 c'est exactement le même :)

def isPossibleDivide(nums, k):
    if len(nums) % k != 0:
        return False

    card_count = {}
    for card in nums:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1

    sorted_cards = sorted(card_count)

    for card in sorted_cards:
        while card in card_count and card_count[card] > 0:
            for i in range(k):
                current_card = card + i
                if current_card not in card_count or card_count[current_card] <= 0:
                    return False
                card_count[current_card] -= 1
                if card_count[current_card] == 0:
                    del card_count[current_card]

    return True