"""Print an deck of cards using emojis"""

suits = [
    spades := "♠️",
    clubs := "♣️",
    hearts := "♥️",
    diamonds := "♦️",
]
values = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

print("Deck of Cards")
for suit in suits:
    print()
    for value in values:
        print(f"{value}{suit} ,", end=" ")
