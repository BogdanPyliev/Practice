def beginning_zeros(number: str) -> int:
    # your code here
    tmp = 0
    for i in number:
        if i == "0":
            tmp+=1
        else:
            return tmp
    return tmp


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))