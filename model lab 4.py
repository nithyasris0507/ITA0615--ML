# EM Algorithm (Coin Toss Example)

coinA = 0.6
coinB = 0.5
data = [1,0,1,1,0,1]   # 1 = Head, 0 = Tail

for _ in range(5):
    headsA = headsB = tailsA = tailsB = 0

    for toss in data:
        probA = coinA if toss==1 else (1-coinA)
        probB = coinB if toss==1 else (1-coinB)
        total = probA + probB

        headsA += (probA/total) * toss
        tailsA += (probA/total) * (1-toss)
        headsB += (probB/total) * toss
        tailsB += (probB/total) * (1-toss)

    coinA = headsA / (headsA + tailsA)
    coinB = headsB / (headsB + tailsB)

print("Final Coin A probability:", coinA)
print("Final Coin B probability:", coinB)
