def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    if not text[-1]  == "." :
        text += "."
    return text[0].upper()+text[1:]


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    