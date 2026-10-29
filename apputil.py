from collections import defaultdict
import numpy as np

class MarkovText(object):

    def __init__(self, corpus):
        """ Initialize the MarkovText object with a given corpus."""
        self.corpus = corpus
        # Initialize a defaultdict to store the terms
        self.term_dict = defaultdict(list)

    def get_term_dict(self):
        """ Build a dictionary of terms and successors corpus"""
        list = (t.text for t in self.term_dict)
        # Spliting the corpus into tokens
        tokens = self.corpus.split()
        # Iterate through the tokens and populate the term_dict with successors
        for i in range(len(tokens) - 1):
            # Get the current token and the next token
            current_token = tokens[i]
            # Get the next token and append it to the list for the current token
            next_token = tokens[i + 1]
            # Append the next token to the list for the current token in the term_dict
            self.term_dict[current_token].append(next_token)

        return self.term_dict


    def generate(self, seed_term=None, term_count=15):
        """ Generate a sequence of terms based on the Markov model."""
        if not self.term_dict:
            self.get_term_dict()
        # Check if the seed_term is in the term_dict
        if seed_term is not None and seed_term not in self.term_dict:
            raise ValueError(f"{seed_term!r} is not in the corpus")
        # Check if term_count is valid and if the term_dict is not empty
        if term_count <= 0 or not self.term_dict:
            return ""
        # Randomly select a starting term from the term_dict
        if seed_term is None:
            current = np.random.choice(list(self.term_dict.keys()))
        else:
            # Use the provided seed_term as the starting term
            current = seed_term
        # Generate the sequence of terms
        output = [current]
        # Generate the next terms based on the current term
        for _ in range(term_count - 1):
            # Get the list of possible next words for current term
            next_words = self.term_dict.get(current, [])
            if not next_words:
                break
            # Randomly select the next word from the list of possible next words
            current_word = np.random.choice(next_words)
            # Append selected next word to the output list and update the current term
            output.append(current_word)
        # Return the generated sequence of terms as a single string
        return " ".join(output)
