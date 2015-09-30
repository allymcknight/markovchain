from random import choice

import sys

source_text = sys.argv[1]

def open_and_read_file(source_text):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    source_text = open(source_text).read()

    return source_text


def make_chains(text_string):
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
    for i in range(len(words) - 2):
        if (words[i], words[i+1]) in chains:
            chains[words[i], words[i+1]].append(words[i+2])
        else:
            chains[words[i], words[i+1]] = [words[i+2]]

    return chains
    print chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    tuple_key = (choice(chains.keys()))
    text = " ".join(tuple_key)

    # for tuple_key in chains:
    #     if tuple_key in chains:
    while tuple_key in chains:
        try:
            value = choice(chains[tuple_key])
            text = text + " " + value
            tuple_key = (tuple_key[1], value)
        except KeyError:
            break
        
    return text

# #input_path = "dracula.txt"

# # Open the file and turn it into one long string
input_text = open_and_read_file(source_text)

# # Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)
print random_text    