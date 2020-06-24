from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    try:
        items.append(items[0])
        items.pop(0)
        return items
    except IndexError:     
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))