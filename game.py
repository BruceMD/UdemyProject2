from tkinter import *
from random import *


money = 1000
hand = []
dHand = []

suite = ["H", "D", "S", "C"]
card = ["A", '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
deck = []
for d in range(6):
    for s in suite:
        for n in card:
            deck.append((n, s))
newDeck = deck
shuffle(newDeck)
print(newDeck)

count = 0
hitNum = 0
hitNumD = 0
labelNext1 = Label(font=("Courier", 20), height=2, width=3)
labelNext2 = Label(font=("Courier", 20), height=2, width=3)
labelNext3 = Label(font=("Courier", 20), height=2, width=3)

labelYouHandTotal = Label(pady=5, font=("Courier", 20), bg='blue')
labelDealerHandTotal = Label(pady=5, font=("Courier", 20), bg='blue')

def deal():
    global count
    if count > 120:
        shuffle(newDeck)
        count = 0

    global hitNum, hitNumD
    global labelNext1, labelNext2, labelNext3
    global labelNextD1, labelNextD2, labelNextD3, labelNextD4
    global hand, dHand

    hand, dHand = [], []

    try:
        labelNext1.place_forget()
        labelNext2.place_forget()
        labelNext3.place_forget()
    except:
        pass
    try:
        labelNextD1.place_forget()
        labelNextD2.place_forget()
        labelNextD3.place_forget()
        labelNextD4.place_forget()
    except:
        pass

    hitNum = 0
    hitNumD = 0
    labelP1 = Label(middleFrameLeft, text=newDeck[count], font=("Courier", 20), height=2, width=3)
    hand.append(newDeck[count][0])
    labelP2 = Label(middleFrameLeft, text=newDeck[count+1], font=("Courier", 20), height=2, width=3)
    hand.append(newDeck[count+1][0])
    labelD = Label(middleFrameRight, text=newDeck[count+2], font=("Courier", 20), height=2, width=3)
    dHand.append(newDeck[count+2][0])
    count += 3

    check(hand)

    global labelYouHandTotal, labelDealerHandTotal
    try:
        labelYouHandTotal.place_forget()
        labelDealerHandTotal.place_forget()
    except:
        pass
    labelYouHandTotal = Label(middleFrameLeft, text=check(hand), pady=5, font=("Courier", 20), bg='blue')
    labelYouHandTotal.place(x=230, y=200)
    labelDealerHandTotal = Label(middleFrameRight, text=check(dHand), pady=5, font=("Courier", 20), bg='yellow')
    labelDealerHandTotal.place(x=230, y=200)

    labelP1.place(x=10, y=50)
    labelP2.place(x=80, y=50)
    labelD.place(x=10, y=50)


def hit():
    global count
    global hitNum
    global labelNext1, labelNext2, labelNext3
    global hand
    if hitNum < 3:
        count += 1
        if hitNum == 0:
            labelNext1 = Label(middleFrameLeft, text=newDeck[count], font=("Courier", 20), height=2, width=3)
            labelNext1.place(x=150, y=50)
            hitNum +=1
        elif hitNum == 1:
            labelNext2 = Label(middleFrameLeft, text=newDeck[count], font=("Courier", 20), height=2, width=3)
            labelNext2.place(x=220, y=50)
            hitNum += 1
        else:
            labelNext3 = Label(middleFrameLeft, text=newDeck[count], font=("Courier", 20), height=2, width=3)
            labelNext3.place(x=290, y=50)
            hitNum += 1
        hand.append(newDeck[count][0])

        global labelYouHandTotal
        labelYouHandTotal.place_forget()
        labelYouHandTotal = Label(middleFrameLeft, text=check(hand), pady=5, font=("Courier", 20), bg='blue')
        labelYouHandTotal.place(x=230, y=200)

        if bust(check(hand)):
            print("You lose\nPlease press Deal")

    else:
        stand()


def stand():
    global count
    global hitNumD
    global labelNextD1, labelNextD2, labelNextD3, labelNextD4
    global hand, dHand
    print("CHECKING STEP: {}".format(dHand))
    while check(dHand) < 17:
        if hitNumD < 4:
            count += 1
            if hitNumD == 0:
                labelNextD1 = Label(middleFrameRight, text=newDeck[count], font=("Courier", 20), height=2, width=3)
                labelNextD1.place(x=80, y=50)
                hitNumD += 1
            elif hitNumD == 1:
                labelNextD2 = Label(middleFrameRight, text=newDeck[count], font=("Courier", 20), height=2, width=3)
                labelNextD2.place(x=150, y=50)
                hitNumD += 1
            elif hitNumD == 2:
                labelNextD3 = Label(middleFrameRight, text=newDeck[count], font=("Courier", 20), height=2, width=3)
                labelNextD3.place(x=220, y=50)
                hitNumD += 1
            else:
                labelNextD4 = Label(middleFrameRight, text=newDeck[count], font=("Courier", 20), height=2, width=3)
                labelNextD4.place(x=290, y=50)
                hitNumD += 1
            dHand.append(newDeck[count][0])
            print(check(dHand))

        global labelDealerHandTotal
        labelDealerHandTotal.place_forget()
        labelDealerHandTotal = Label(middleFrameRight, text=check(dHand), pady=5, font=("Courier", 20), bg='yellow')
        labelDealerHandTotal.place(x=230, y=200)

        if check(dHand) > 21:
            print("Dealer goes bust, you win!")
            break
    if check(dHand) < 22 and check(hand) < 22:
        if check(dHand) > check(hand):
            print("Dealer wins!")
        elif check(dHand) == check(hand):
            print("Push")
        else:
            print("You win!")
######################################################################################################################

def check(h):
    total = 0
    dic = {'A': 1, 'T':10, 'J':10, 'Q':10, 'K':10}
    ace = False
    print(h)
    for c in h:
        if c == 'A':
            ace = True
        if c in dic:
            total += dic[c]
        else:
            total += int(c)

    if ace and total <= 11:
        total += 10
    print(total)
    return total


def bust(x):
    if x > 21:
        print("BUST")
        return True
    return False



mWindow = Tk()
mWindow.geometry("1000x500")
mWindow.title("Milestone Project 2 - Udemy Complete Python 3 Bootcamp")

for i in range(10):
    mWindow.columnconfigure(i, weight=1)
for j in range(8):
    mWindow.rowconfigure(j, weight=1)

topFrame = Frame(mWindow, bg="red")
topFrame.grid(row=0, column=0, rowspan=1, columnspan=10, sticky = W+E+N+S)
middleFrameLeft = Frame(mWindow, bg="blue")
middleFrameLeft.grid(row=1, column=0, rowspan=4, columnspan=5, sticky = W+E+N+S)
middleFrameRight = Frame(mWindow, bg="yellow")
middleFrameRight.grid(row=1, column=5, rowspan=4, columnspan=5, sticky = W+E+N+S)
bottomFrame = Frame(mWindow, bg="green")
bottomFrame.grid(row=5, column=0, rowspan=2, columnspan=10, sticky = W+E+N+S)


labelHeader = Label(topFrame, text="BLACKJACK", font=("Courier", 40), bg="red")
labelDealer = Label(middleFrameRight, text="DEALER", pady=5, font=("Courier", 20), bg='yellow')
labelYou = Label(middleFrameLeft, text="YOU", pady=5, font=("Courier", 20), bg='blue')
labelYouHandTotal = Label(middleFrameLeft, text=check(hand), pady=5, font=("Courier", 20), bg='blue')

labelHeader.place(x=225, y=0)
labelDealer.pack()
labelYou.pack()
labelYouHandTotal.place(x=230, y=200)

buttonDeal = Button(bottomFrame, text="DEAL", height=3, width=8, command=deal)
buttonHit = Button(bottomFrame, text="HIT", height=3, width=8, command=hit)
buttonStand = Button(bottomFrame, text="STAND", height=3, width=8, command=stand)

buttonDeal.place(x=50, y=30)
buttonHit.place(x=230, y=30)
buttonStand.place(x=330, y=30)

mWindow.mainloop()
