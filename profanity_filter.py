def censor_text(text):
    # List of curse words
    curse_words = ["darn", "dang", "freakin", "heck", "shoot"]

    # Replace each curse word with stars of the same length
    for word in curse_words:
        text = text.replace(word, "*" * len(word))

    return text


# Main program
user_input = input("Enter some text: ")
censored = censor_text(user_input)
print("\n" + censored)
