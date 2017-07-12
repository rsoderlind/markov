"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    green_eggs_file = open(file_path)
    green_eggs_string = green_eggs_file.read()

    return green_eggs_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
         
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    

    words_string = text_string.replace("\n", " ")
    words_string = words_string.rstrip() 
    words = words_string.split(" ")
    
    for i in range(len(words)):
        key = (words[i], words[(i + 1)%len(words)])
        if not key in chains:
            chains[key] = []
        chains[key].append(words[(i + 2)%len(words)])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    count = 0
    #repeat
        # pick random key from dictionary
        #break loop if key[0] is uppercased
        #from random pair search dict for matching key
        # use associated value for key and add to tuple 
        #add condition to end or loop won't continue forever 
    # print chains
    current_bigram = choice(chains.keys())
    for item in current_bigram:
        words.append(item)

    while count < len(chains):
        
        print current_bigram

        print chains[current_bigram]

        added_word = choice(chains[current_bigram])
        words.append(added_word)
        current_bigram = (current_bigram[1], added_word)
        
        count = count + 1
        
 



    


words = []


    #return " ".join(words) next_wo


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print chains 
# Produce random text
random_text = make_text(chains)

print random_text
