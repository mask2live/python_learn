
def inputStatement():
    tags = ("how", "what", "why", "where", "which", "when", "is", "are", "were", "was", "do", "did", "does", "shall")
    string = ""
    while True:
        content = input("Say something: ")
        if content != "\\end":
            if content.startswith(tags):
                content = "{}? ".format(content.capitalize())
            else :
                content = "{}. ".format(content.capitalize())
            string = string + content
        else:
            break
    print(string)

if __name__ == "__main__":
    
    inputStatement()