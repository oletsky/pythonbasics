#Dictionaries in Python

prices={"water":100, "bread":200, "beer":10}
print(prices)
prices["cheese"]=300
print(prices)
del prices["beer"]
print("Eventually")
for key in prices:
    print(key," - ",prices[key])