import unittest
from algorithms.rabin_karp_algorithm import RabinKarpSearch


class TestRabinKarp(unittest.TestCase):

    def setUp(self):
        self.rabin_karp = RabinKarpSearch()
        self.hash_functions = ['polynomial', 'simple', 'xor']

    def run_test(self, text, pattern, expected):
        for hash_func in self.hash_functions:
            with self.subTest(hash_func=hash_func):
                result = self.rabin_karp.rabin_karp_search(text, pattern, hash_func)
                self.assertEqual(result, expected)

    def test_pattern_found_at_start(self):
        text = 'hello world'
        pattern = 'hello'
        self.run_test(text, pattern, 0)

    def test_pattern_found_in_middle(self):
        text = 'hello world'
        pattern = 'lo'
        self.run_test(text, pattern, 3)

    def test_pattern_found_at_end(self):
        text = 'hello world'
        pattern = 'world'
        self.run_test(text, pattern, 6)

    def test_pattern_not_found(self):
        text = 'hello world'
        pattern = 'hallo'
        self.run_test(text, pattern, -1)

    def test_empty_text(self):
        text = ''
        pattern = 'hi'
        self.run_test(text, pattern, -1)

    def test_empty_pattern(self):
        text = 'hello world'
        pattern = ''
        self.run_test(text, pattern, 0)

    def test_pattern_longer_than_text(self):
        text = 'hello'
        pattern = 'hello world'
        self.run_test(text, pattern, -1)

    def test_repeat_many_times(self):
        text = "abcabcabc"
        pattern = "abc"
        self.run_test(text, pattern, 0)

    def test_case_sensitivity(self):
        text = 'Hello world'
        pattern = 'hello'
        self.run_test(text, pattern, -1)

    def test_whitespace_in_pattern(self):
        text = "hello world"
        pattern = " "
        self.run_test(text, pattern, 5)

    def test_numeric_pattern(self):
        text = "abc123def"
        pattern = "123"
        self.run_test(text, pattern, 3)


if __name__ == "__main__":
    unittest.main()
