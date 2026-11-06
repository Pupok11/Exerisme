"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    Parameters:
        word: The root word.

    Returns:
        Root word prepended with 'un'.
    """
    return 'un' + word
    

def make_word_groups(vocab_words: list[str]) -> str:
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words: Vocabulary words with prefix at first index.

    Returns:
        Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.
    """
    prefix_and_symbol = ' :: ' + vocab_words[0]
    return prefix_and_symbol.join(vocab_words)


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word: Word to remove suffix from.

    Returns:
        Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'
    """
    if word.endswith('ness'):
        words = word.replace('ness', '')
    if words.endswith('i'):
        words = words.replace('i', 'y')
    return words
    

    

def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence: The word used in a sentence as an adjective.
        index: Index of the adjective to remove and transform.

    Returns:
        The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'
    """
    if index == -1:
        sentence = sentence.split()[index].replace('.', '')
    return sentence.split()[index] + 'en'