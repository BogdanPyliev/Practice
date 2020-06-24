def max_digit(number: int) -> int:
    # your code here
    return int(max(str(number)))


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))