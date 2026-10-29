from collections import defaultdict
import numpy as np

class MarkovText(object):

    def __init__(self, corpus):
        """ Initialize the MarkovText object with a given corpus."""
        self.corpus = corpus
        self.term_dict = defaultdict(list)

    def get_term_dict(self):
        """ Build a dictionary of terms and successors corpus"""
        list = (t.text for t in self.term_dict)

        tokens = self.corpus.split()

        for i in range(len(tokens) - 1):
            current_token = tokens[i]
            next_token = tokens[i + 1]
            self.term_dict[current_token].append(next_token)

        return self.term_dict


    def generate(self, seed_term=None, term_count=15):
        """ Generate a sequence of terms based on the Markov model."""
        if not self.term_dict:
            self.get_term_dict()

        if seed_term is not None and seed_term not in self.term_dict:
            raise ValueError(f"{seed_term!r} is not in the corpus")

        if term_count <= 0 or not self.term_dict:
            return ""
        if seed_term is None:
            current = np.random.choice(list(self.term_dict.keys()))
        else:
            current = seed_term

        output = [current]

        for _ in range(term_count - 1):
            next_words = self.term_dict.get(current_word, [])
            if not next_words:
                break

            current_word = np.random.choice(next_words)
            output.append(current_word)
        return " ".join(output)
