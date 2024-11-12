names = ["Daeju", "Richard", "Kevin", "James", "Warren", "Hwanmin", "Donghyuk", "Taehoon", "Taeyoon", "Beomkyu", "Sieon", "Devyn", "Seoyoung", "Hayoung"]
#print(names)
#print(len(names))

bDays = ["05_07_06", "05_12_13", "07_08_17", "06_08_25", "06_09_28", "06_05_23", "07_10_01", "06_02_01", "06_07_05", "07_06_02", "06_03_17", "05_11_17", "06_04_03", "07_07_11"]
#print(len(bDays))
#print(bDays)

def makeDict(given01: list, given02: list) -> dict:
    result = {}
    for i in range(len(given01)):
        result[given01[i]] = given02[i]
    
    return result

print(makeDict(names, bDays))

