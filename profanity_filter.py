def censor_text(text):
    # List of curse words
    curse_words = ["darn", "dang", "freakin", "heck", "shoot"]

    result_words = []
    for word in text.split():
        # Compare lowercase version
        if word.lower() in curse_words:
            result_words.append("*" * len(word))
        else:
            result_words.append(word)

    return " ".join(result_words)


# Main program
user_input = input("Enter some text: ")
censored = censor_text(user_input)
print("\n" + censored)
