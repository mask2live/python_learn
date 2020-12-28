def addNum(a : int, b : int):
    return a + b

def upperSort(args):
    args = sorted([i.upper() for i in args])
    return args
    # return sorted(args)

def upperSort1(*args):
    return sorted([i.upper() for i in args])

def starred(*args):
    print(type(args))
    for i in args:
        print(i)
    return args

def kwstarred(**kwargs):
    print(type(kwargs))
    return kwargs

if __name__ == "__main__":
    print(addNum(4, 7))
    print(addNum("abc", "def"))
    ss = [9, 7]
    print(addNum(*ss))
    print(starred(ss))
    print("------------------------------")
    sts = ["snow", "glacier", "iceberg"]
    print(upperSort1(*sts))
    print("------------------------------")
    print(kwstarred(a=9, b=4))
    dictTest = {"a":1, "b":2, "c":3, "d":4}
    print(kwstarred(**dictTest))