

def read_from_file(file_path):

    with open(file_path, 'r') as f:
        content = f.read(10)
        print(content)
        print(type(content))


def write_to_file(file_path):

    with open(file_path, 'a+') as f:
        f.write('\nwhich is your favorite?')
        f.seek(0)
        print(f.read())


def getStringCount(character, filepath):

    with open(filepath, 'r') as f:
        content = f.read()
    # return the count of character in the file
    return content.count(character)


# a+ -- it put cursor to the end
# if you want to get content in the file, you need to change position of the cursor
def insertTimes(filepath, n):
    with open(filepath, 'a+') as f:
        f.seek(0)
        content = f.read()
        for i in range(n):
            f.write(content)
    

if __name__ == '__main__':
    # read_from_file('FileProcessing/test.txt')
    # write_to_file('FileProcessing/test.txt')
    # read_from_file('FileProcessing/test.txt')

    insertTimes('FileProcessing/test.txt', 3)