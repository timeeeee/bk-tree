import unittest

from bktree import *


class TestLevenshteinDistanceRecursive(unittest.TestCase):
    def test_first_word_empty(self):
        a = ""
        b = ""
        for n in range(10):
            self.assertEqual(levenshtein_recursive(a, b), n)
            b += "x"

    def test_second_word_empty(self):
        a = ""
        b = ""
        for n in range(10):
            self.assertEqual(levenshtein_recursive(a, b), n)
            a += "x"

    def test_words_equal(self):
        for word in "A testcase is created by subclassing TestCase".split():
            self.assertEqual(levenshtein_recursive(word, word), 0)

    def test_deletion(self):
        word1 = "recursive"
        for n, char in enumerate(word1):
            word2 = word1[:n] + word1[n+1:]

            self.assertEqual(levenshtein_recursive(word1, word2), 1)
            self.assertEqual(levenshtein_recursive(word2, word1), 1)

    def test_replacement(self):
        word1 = "iterative"
        for n, char in enumerate(word1):
            word2 = word1[:n] + "x" + word1[n+1:]

            self.assertEqual(levenshtein_recursive(word1, word2), 1)
            self.assertEqual(levenshtein_recursive(word2, word1), 1)

    def test_insertion(self):
        word1 = "someone"
        for n, _ in enumerate(word1):
            word2 = word1[:n] + "x" + word1[n:]

            self.assertEqual(levenshtein_recursive(word1, word2), 1)
            self.assertEqual(levenshtein_recursive(word2, word1), 1)

    def test_insert_and_delete(self):
        self.assertEqual(levenshtein_recursive("watch", "xwatc"), 2)
        self.assertEqual(levenshtein_recursive("watch", "atchx"), 2)
        self.assertEqual(levenshtein_recursive("xwatc", "watch"), 2)
        self.assertEqual(levenshtein_recursive("atchx", "watch"), 2)


if __name__ == "__main__":
    unittest.main()
