def remove_fourth_character(word: str) -> str:
    bf = word[:3]
    af = word[4:]
    new_word = bf+af
    return new_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
