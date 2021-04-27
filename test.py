import unittest

from bktree import *


class TestBKTree(unittest.TestCase):
    def test_insert_one(self):
        tree = BKTree()
        tree.insert("recursive")
        self.assertTupleEqual(tree.root, ("recursive", {}))

    def test_insert_two(self):
        tree = BKTree()
        tree.insert("one")
        tree.insert("two")
        self.assertTupleEqual(tree.root, ("one", {3: ("two", {})}))

    def test_wikipedia_example(self):
        tree = BKTree()
        words = [
            "book", "books", "cake", "boo", "cape", "cart", "boon", "cook"]
        for word in words:
            tree.insert(word)

        expected = (
            "book", {
                1: (
                    "books", {
                        2: (
                            "boo", {
                                1: ("boon", {}),
                                2: ("cook", {})})}),
                4: (
                    "cake", {
                        1: ("cape", {}),
                        2: ("cart", {})})})
        self.assertTupleEqual(tree.root, expected)

    def test_lookup_one_word(self):
        tree = BKTree()
        tree.insert("levenshtein")
        self.assertEqual(tree.closest_match("levenshtein"), "levenshtein")

    def test_lookup_two_words(self):
        tree = BKTree()
        tree.insert("three")
        tree.insert("one")
        self.assertEqual(tree.closest_match("two"), "one")

    def test_lookup_no_results(self):
        tree = BKTree()
        tree.insert("one")
        tree.insert("two")
        self.assertIsNone(tree.closest_match("three", max_distance=2))

    def test_lookup_exact_match(self):
        tree = BKTree()
        words = [
            "book", "books", "cake", "boo", "cape", "cart", "boon", "cook"]
        
        for word in words:
            tree.insert(word)

        self.assertEqual(tree.closest_match("boo", max_distance=1), "boo")


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
