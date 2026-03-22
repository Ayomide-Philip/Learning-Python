scores = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 20, 90, 199, 10000, 5050, 7000]

highestScore = 0

for score in scores:
    if highestScore < score:
        highestScore = score

print(highestScore)
