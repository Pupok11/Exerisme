"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title: str) -> str:
    """Convert the first letter of each word in the title to uppercase if needed.

    Parameters:
        title: Essay title that needs title casing.

    Returns:
        The title string in title case (first letters capitalized).
    """

    return title.title()


def check_sentence_ending(sentence: str) -> str:
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence: A sentence to check.

    Returns:
        Is the sentence punctuated correctly?
    """
    return sentence.endswith('.')

    


def clean_up_spacing(sentence: str) -> str:
    """Trim any leading or trailing whitespace from the sentence.

    Parameters:
        sentence: A sentence to clean of leading and trailing space characters.

    Returns:
        A sentence that has been cleaned of leading and trailing space characters.
    """

    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence: A sentence to replace words in.
        old_word: The word to replace.
        new_word: The replacement word.

    Returns:
        Input sentence with new words in place of old words.
    """
    return sentence.replace(old_word, new_word)

    
