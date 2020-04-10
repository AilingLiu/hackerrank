# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe."""

from collections import Counter

def calPrice(shoes_arr, buy_arr, price_arr):

    total = 0

    shoes_stock = Counter(shoes_arr)

    for i in range(len(buy_arr)):
        if shoes_stock[buy_arr[i]]:
            total += price_arr[i]
            shoes_stock[buy_arr[i]]-=1
    
    return total


if __name__ == '__main__':


    num = int(input())
    shoes = list(map(int, input().split()))
    customers = int(input())
    shoes_need = []
    price = []

    for i in range(customers):

        a, b = map(int, input().split())
        shoes_need.append(a)
        price.append(b)

    total = calPrice(shoes, shoes_need, price)
    print(total)

