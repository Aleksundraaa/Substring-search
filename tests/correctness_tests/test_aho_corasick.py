import unittest
from algorithms.aho_corasick_algorithm import AhoCorasickSearch

class TestAhoCorasick(unittest.TestCase):
    def setUp(self):
        self.aho_corasick = AhoCorasickSearch(["hello", "world", "lo", "abc", "123", " "])

    def test_pattern_found_at_start(self):
        text = 'hello world'
        pattern = 'hello'
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, 0)

    def test_pattern_found_in_middle(self):
        text = 'hello world'
        pattern = 'lo'
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, 3)

    def test_pattern_found_at_end(self):
        text = 'hello world'
        pattern = 'world'
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, 6)

    def test_pattern_not_found(self):
        text = 'hello world'
        pattern = 'hallo'
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, -1)

    def test_empty_text(self):
        text = ''
        pattern = 'hello'
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, -1)

    def test_empty_pattern(self):
        text = 'hello'
        pattern = ''
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, 0)

    def test_pattern_longer_than_text(self):
        text = 'hello'
        pattern = 'hello world'
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, -1)

    def test_repeat_many_times(self):
        text = "abcabcabc"
        pattern = "abc"
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, 0)

    def test_case_sensitivity(self):
        text = "Hello World"
        pattern = "hello"
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, -1)

    def test_whitespace_in_pattern(self):
        text = "hello world"
        pattern = " "
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, 5)

    def test_numeric_pattern(self):
        text = "abc123def"
        pattern = "123"
        result = self.aho_corasick.aho_corasick_search(text, pattern)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
