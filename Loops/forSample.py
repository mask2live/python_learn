nums = [1,2,3,4,5.0,8.3]
def aFor():
    for i in nums:
        print(i)

def forWithType():
    for i in nums:
        if isinstance(i, float):
            print(i)

def forWithTypeAndValue():
    for i in nums:
        if isinstance(i, int) and i > 2:
            print(i)


if __name__ == "__main__":
    aFor()
    print("_______________")
    forWithType()
    print("_______________")
    forWithTypeAndValue()
