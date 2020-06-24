def end_zeros(num: int) -> int:
    # your code here
    tmp = 0
    for i in reversed(str(num)):
        if i == "0":
            tmp+=1
        else:
            return tmp
    return tmp


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))