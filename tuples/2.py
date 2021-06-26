a = ['1','2','3','4']
print( map(list,a))
print (map(int,a))

print(list(map(list,a)))
print(list(map(int,a)))

print("************************************")
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(date)

year,month,day = date
print(year,month,day)



prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
print(min_price)
print(max_price)