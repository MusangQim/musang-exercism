"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words."""
    result = []
    prefix = vocab_words[0]
    result.append(prefix)
    for word in vocab_words[1:]:
        result.append(prefix + word)
    return " :: ".join(result)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""
    if word.endswith("iness"):
        return word[:-5] + "y"
    return word[:-4]


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    words = sentence.split()
    word = words[index].strip(".")
    return word + "en"
