dictsA = {"aa": 1, "ab": 2, "ac": 3, "ad": 4}
def forItems():
    for k, v in dictsA.items():
        print(f"key: {k}, value: {v}")

def forItemsPair():
    for pair in dictsA.items():
        print(f"key: {pair[0]}, value: {pair[1]}")

def forKey():
    for k in dictsA.keys():
        print(k)

def forValue():
    for v in dictsA.values():
        print(v)

def forDict():
    for d in dictsA:
        print(d.replace("a", "x"))


if __name__ == "__main__":
    print("-------items--------")
    forItems()
    print("-------pair--------")
    forItemsPair()
    print("-------keys--------")
    forKey()
    print("-------values--------")
    forValue()
    print("-------none--------")
    forDict()