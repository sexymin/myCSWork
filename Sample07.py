items = ["Apple", "Banana", "Kiwi", "Orange"]
price = [22.3, 54.1, 13.6, 4.6]

def makeDict(given01: list, given02: list) -> dict:
    result = {}
    for i in range(len(given01)):
        result[given01[i]] = given02[i]
    
    return result

################## RUN ###################
print(makeDict(items, price))
