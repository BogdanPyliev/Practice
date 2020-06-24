def nearest_value(values: set, one: int) -> int:
    # your code here
    return min(values,key=lambda x: (abs(x-one),x))
  
    


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
