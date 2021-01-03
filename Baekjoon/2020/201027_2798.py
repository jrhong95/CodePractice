N, max_sum = map(int, input().split())
cards = list(map(int, input().split()))
cards_len = len(cards)
max_card_sum = 0

for x in range(cards_len - 2):
    for y in range(x + 1, cards_len - 1):
        for z in range(y + 1, cards_len):
            if cards[x] + cards[y] + cards[z] <= max_sum:
                max_card_sum = max(max_card_sum, cards[x] + cards[y] + cards[z])

print(max_card_sum)