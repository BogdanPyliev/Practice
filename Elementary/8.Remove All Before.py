from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    try:
        return items[items.index(border):]
    except  ValueError:
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))