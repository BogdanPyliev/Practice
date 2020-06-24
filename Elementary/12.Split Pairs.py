def split_pairs(a):
    # your code here
    for i in range(0, len(a), 2):
        try:
            yield a[i]+a[i+1]
        except IndexError:
            yield a[i]+'_'


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))