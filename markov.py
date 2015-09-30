from random import choice

import sys

source_text = sys.argv[1]

def open_and_read_file(source_text):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(source_text) as file:
        source_text = file.read()

    return source_text


def make_chains(text_string, n):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.split()
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        
        if key in chains:
            chains[key].append(words[i+n])

        else:
            chains[key] = [words[i+n]]

    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    tuple_key = choice(chains.keys())
    text = " ".join(tuple_key)

    # for tuple_key in chains:
    #     if tuple_key in chains:
    while tuple_key in chains:

            value = choice(chains[tuple_key])
            text = text + " " + value
            tuple_key = tuple_key[1:] + (value,)

    return text

# #input_path = "dracula.txt"

# # Open the file and turn it into one long string
input_text = open_and_read_file(source_text)

# # Get a Markov chain
chains = make_chains(input_text, 3)
# # Produce random text
random_text = make_text(chains)
print random_text    