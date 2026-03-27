import os

print("Welcome to the secret auction program")


def getBidderWithHighestAmount(bidList):
    highestBid = 0
    highestBidderName = ""
    for i in range(0, len(bidList)):
        if highestBid < bidList[i]["amount"]:
            highestBid = bidList[i]["amount"]
            highestBidderName = bidList[i]["name"]
    return {"name": highestBidderName, "amount": highestBid}


isAuctionEnd = False
bidderList = []

while not isAuctionEnd:
    name = input("What is your name?:")
    biddingAmount = int(input("What is your bid?: $"))
    bidderList.append({"name": name, "amount": biddingAmount})
    areThereAnyOtherBidders = input(
        "Are there any other bidders? Type 'yes' or 'no'."
    ).lower()
    if areThereAnyOtherBidders == "yes":
        print("Continuing the good work")
        os.system("cls")
    else:
        isAuctionEnd = not isAuctionEnd
        winner = getBidderWithHighestAmount(bidderList)
        print(f"The Winner is {winner['name']} with an amount of ${winner["amount"]} ")
