

def count_words(text):
    """
    Accepts text as a parameter, and returns a dictionary of the word lengths in it.
    :param text: The text.
    :return: A dictionary mapping word lengths to the number of words with that length.
    """
    a_till_z_text = ''.join(x for x in text if x.isspace() or x.isalpha())
    word_lengths = {word: len(word) for word in a_till_z_text.split()}
    return word_lengths


if __name__ == '__main__':
    my_text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    dictionary = count_words(my_text)

    print("The length of each word in the text is: ")
    for key, value in dictionary.items():
        print(str(key) + ': ' + str(value))

