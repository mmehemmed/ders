import random
import os
a = ["Red", "Green", "Blue", "Yellow"]
b = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, "Block", "Block", "Reverse", "Reverse", "+2", "+2"]
c = ["Wild", "Wild +4"]

def createDeck():
    deck = []
    for i in range(len(a)):
        for j in range(len(b)):
            deck.append(a[i] + " " + str(b[j]))
    for i in range(4):
        deck.append(c[0])
        deck.append(c[1])
    random.shuffle(deck)
    return deck

def dealCard(number, deck):
    cards = []
    for i in range(number):
        a = random.randint(0, len(deck) - 1) 
        cards.append(deck[a])
        deck.pop(a)
    return cards

def playCard(playerDeck, cardIndex):
    lastPlayedCards.append(playerDeck[cardIndex-1])
    playerDeck.pop(cardIndex-1)

lastPlayedCards = []
deck = createDeck()
player1 = dealCard(7, deck)
player2 = dealCard(7, deck)

running = True
while running:
    if(len(lastPlayedCards)>=1):
        print("Oynanıldı:   " + lastPlayedCards[len(lastPlayedCards)-1])
    print("PLayer 1")
    print(player1)
    index = input("Hansi karti oynamaq istiyirsiz:   ")


    try:
        index = int(index)
    except ValueError:
        print("Xahish edirik, etibarlı bir rəqəm daxil edin.")
        continue 

    if index != 99:
        if player1[index].endswith("Block"):
            pass
        elif player1[index].endswith("Reverse"):
            pass
        elif player1[index].endswith("+2"):
            player2.extend(dealCard(2, deck))
        elif player1[index].endswith("+4"):
            if lastPlayedCards and lastPlayedCards[-1].endswith("+4"):
                player2.extend(dealCard(8, deck))
            else:
                player2.extend(dealCard(4, deck))
        playCard(player1, index)
    else:
        lastPlayedCards.append("Pass")
        player1.extend(dealCard(2, deck))
    os.system('cls')
    print("Player 2")
    print("Oynanıldı:   " + lastPlayedCards[len(lastPlayedCards)-1])
    print(player2)
    index = input("Hansi karti oynamaq istiyirsiz:   ")

   
    try:
        index = int(index)
    except ValueError:
        print("Please enter a reliable number.")
        continue 

    if index != 99:
        if player2[index].endswith("Block"):
            pass
        elif player2[index].endswith("Reverse"):
            pass
        elif player2[index].endswith("+2"):
            player1.extend(dealCard(2, deck))
        elif player2[index].endswith("+4"):
            if lastPlayedCards and lastPlayedCards[-1].endswith("+4"):
                player1.extend(dealCard(8, deck))
            else:
                player1.extend(dealCard(4, deck))
        playCard(player2, index)
    else:
        lastPlayedCards.append("Pass")
        player2.extend(dealCard(2, deck))
    os.system('cls')
    if(len(player1) == 0):
        print("Player 1 won")
    if(len(player2) == 0):
        print("Player 2 won")