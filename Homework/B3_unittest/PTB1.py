def find_x(a,b):
    if a:
        return -b/a
    elif b:
        return "NONE"
    else:
        return "ALL"

def find_x_2(a,b):
    return -b/a


if __name__ == "__main__":
    print(find_x(5,7))