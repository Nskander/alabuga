from collections import Counter
from icecream import ic


def calculate_diversity(a_collection: list, b_collection: list) -> int:
    a_counter = Counter(a_collection)
    b_counter = Counter(b_collection)
    for card in list(a_counter):
        if card in b_counter:
            common_cards = min(a_counter[card], b_counter[card])
            a_counter[card] -= common_cards
            b_counter[card] -= common_cards
            if a_counter[card] == 0:
                del a_counter[card]
            if b_counter[card] == 0:
                del b_counter[card]
    diversity = sum(a_counter.values()) + sum(b_counter.values())
    return diversity


n, m, q = map(int, input().split())
a_collection = list(map(int, input().split()))
b_collection = list(map(int, input().split()))
ic(a_collection, b_collection)
for _ in range(q):
    typek, playerk, cardk = input().split()
    cardk = int(cardk)
    if playerk == 'A':
        if typek == '1':
            a_collection.append(cardk)
        else:
            a_collection.remove(cardk)
    else:
        if typek == '1':
            b_collection.append(cardk)
        else:
            b_collection.remove(cardk)
    print(calculate_diversity(a_collection, b_collection), end=' ')
