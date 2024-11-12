'''
Check if it is a triangle or not
Print out the results and return nothing
ex)
True
True
False
False
True
True

'''
triangleList = [(3,3,3), (3,4,5), (5,6,1), (4,5,9), (9,3,1), (3,5,8)]

def checker(givenList: list) -> None:
    for triangle in givenList:
        a, b, c = triangle
        if (a + b > c) and (a + c > b) and (b + c > a):
            print(f"{triangle}: True")  
        else:
            print(f"{triangle}: False")

checker(triangleList)





