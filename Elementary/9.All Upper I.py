def is_all_upper(text: str) -> bool:
    # your code here
    if text.isupper()or text.strip() == "" or text.isdigit() :
        return True
    else:    
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))