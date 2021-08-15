def maxprofit(prices):
    if len(prices) == 0:
        return 0

    minPrice = prices[0]
    maxprofit = 0

    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]

        elif (prices[i] - minPrice) > maxprofit:
            maxprofit = prices[i] - minPrice

    return maxprofit


if __name__ == '__main__':
    prices = [2, 1, 5, 3, 6, 4, 9]
    print(maxproft(prices))
