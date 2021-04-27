import logging

logging.basicConfig(level=logging.WARNING)


class BKTree(object):
    """
    A node is a tuple: (word, subtrees)
    subtrees is a dict with edit distances as keys and child nodes as values
    """
    def __init__(self):
        self.root = None

    def insert(self, word):
        ...

    def lookup(self, word):
        ...


CACHE = {}
def levenshtein_recursive(word1, word2, depth=0):
    cache_key = tuple(sorted([word1, word2]))
    if cache_key in CACHE:
        return CACHE[cache_key]

    indent = "  " * depth
    logging.debug(f"{indent}{word1} vs {word2}")
        
    if len(word1) == 0:
        logging.debug(f"{indent}base case! word1 empty")
        return len(word2)

    if len(word2) == 0:
        logging.debug(f"{indent}base case! word2 empty")
        return len(word1)

    if word1[0] == word2[0]:
        logging.debug(f"{indent}first letters match, recursing on tails")
        result = levenshtein_recursive(word1[1:], word2[1:])
        CACHE[cache_key] = result
        return result

    logging.debug(f"{indent}recursing to find deletion distance")
    deletion_dist = levenshtein_recursive(word1[1:], word2, depth + 1)
    logging.debug(f"{indent}recursing to find insertion distance")
    insertion_dist = levenshtein_recursive(word1, word2[1:], depth + 1)
    logging.debug(f"{indent}recursing to find replacement distance")
    replacement_dist = levenshtein_recursive(word1[1:], word2[1:], depth + 1)
    
    result = min(deletion_dist, insertion_dist, replacement_dist) + 1
    CACHE[cache_key] = result
    logging.debug(f"{indent}calculated result {result}")
    return result
