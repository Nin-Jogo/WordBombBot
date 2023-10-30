import nltk
#nltk.download('words')
from nltk.corpus import words

def contains_sequence(word, seq):
    """
    Check if the word contains the given sequence of letters.
    """
    return seq in word

def find_possible_words(sequence, find_longest=True):
    """
    Find the shortest or longest word that contains the sequence.
    """
    word_list = words.words()
    possible_words = [word for word in word_list if contains_sequence(word, sequence)]
    
    if not possible_words:
        return None  # Return None if no words are found

    if find_longest:
        # Find the longest word
        return max(possible_words, key=len)
    else:
        # Find the shortest word
        return min(possible_words, key=len)

# Example usage
sequence = "flo"
longest_word = find_possible_words(sequence, find_longest=True)
shortest_word = find_possible_words(sequence, find_longest=False)

print(f"Longest Word: {longest_word}")
print(f"Shortest Word: {shortest_word}")