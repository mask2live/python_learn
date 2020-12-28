
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f'Zero division is meaningless, {e}')


def divide2(a, b):
    if b == 0:
        return 'Error, {}'.format(ZeroDivisionError("Zero division is meaningless"))
    else:
        return a / b


if __name__ == '__main__':

    print(divide(2,0))
    print(divide2(3,0))