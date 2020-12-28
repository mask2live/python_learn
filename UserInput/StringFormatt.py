
def sample1():
    username = input("Enter your name: ")
    surname = input("Enter your surname: ")


    print("Hello, %s %s" %  (username,surname))
    print(f"Hello, {username} {surname}") # python 3.6 or later
    print("Hello, {} {}".format(username, surname))


def firstLetterUpper(string: str):
    # first = string[0].upper();
    # return first+string[1:]
    return string.title()

if __name__ == "__main__":
    str = "hisoka"
    print(str.upper())

    print(firstLetterUpper(str))

    print(type(34.0) == int)
    print(isinstance(34.9, float))
    

    # sample1()