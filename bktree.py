import logging
import math

logging.basicConfig(level=logging.WARNING)


class BKTree(object):
    """
    A node is a tuple: (word, subtrees)
    subtrees is a dict with edit distances as keys and child nodes as values
    """
    def __init__(self, tree=None):
        self.root = tree

    def insert(self, word):
        new_node = (word, {})

        if self.root is None:
            self.root = new_node
            return

        # go down the tree until we find this word's parent
        current_node = self.root
        node_word, node_children = current_node
        edit_distance = levenshtein_recursive(word, node_word)
        while edit_distance in node_children:
            current_node = node_children[edit_distance]
            node_word, node_children = current_node
            edit_distance = levenshtein_recursive(word, node_word)

        # add the child
        node_children[edit_distance] = new_node

    def closest_matches(self, word, num_matches, max_distance=math.inf):
        """
        
        """
        ...
        
    def closest_match(self, word, max_distance=math.inf):
        queue = [self.root]
        best_match = None
        best_distance = max_distance
        while len(queue) > 0:
            node_word, node_children = queue.pop()
            distance = levenshtein_recursive(word, node_word)
            if distance < best_distance:
                best_match = node_word
                best_distance = distance

            for distance_to_child, child_node in node_children.items():
                if abs(distance_to_child - distance) < best_distance:
                    queue.append(child_node)

        return best_match

    def __repr__(self):
        return f"BKTree({self.root})"


def levenshtein_distance(word1, word2):
    """
    Wagner-Fischer algorithm
    https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
    """
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
