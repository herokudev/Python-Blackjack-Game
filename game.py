from random import shuffle


def createDeck():
    Deck = []

    faceValues = ["A", "J", "Q", "K"]
    for i in range(4):  # There are 4 different suits of cards
        for card in range(2, 11):  # Adding numbers for each suit of cards
            Deck.append(str(card))

        for card in faceValues:  # Adding mayor cards for each suit
            Deck.append(card)

    return Deck


cardDeck = createDeck()

shuffle = shuffle(cardDeck)

print(cardDeck)
