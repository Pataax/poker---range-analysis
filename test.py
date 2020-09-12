import itertools

suits = "dhsc"
pairs = [
    "AA",
    "QQ",
]
non_pairs = [
    "AK",
]
combinations = {}

for hand in pairs:
    combinations[hand] = [
        (
            hand[0] + suit[0],
            hand[1] + suit[1],
        )
        for suit in itertools.combinations(suits, len(hand))
    ]

for hand in non_pairs:
    combinations[hand] = [
        (
            hand[0] + suit[0],
            hand[1] + suit[1],
        )
        for suit in list(itertools.product(suits, repeat=2))
    ]

print(combinations)