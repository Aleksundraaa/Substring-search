class RabinKarpSearch:

    def __init__(self, prime=101, alphabet_len=256):
        self._prime = prime
        self._alphabet_len = alphabet_len

    def _polynomial_hash_function(self, s, length):
        hash_value = 0
        for i in range(length):
            hash_value = (hash_value * self._alphabet_len + ord(s[i])) % self._prime
        return hash_value

    def _update_hash_polynomial(self, current_hash, old_char, new_char, hash_value):
        current_hash = (current_hash - ord(old_char) * hash_value) % self._prime
        current_hash = (current_hash * self._alphabet_len + ord(new_char)) % self._prime
        if current_hash < 0:
            current_hash += self._prime
        return current_hash

    def _simple_hash_function(self, s, length):
        hash_value = 0
        for i in range(length):
            hash_value = (hash_value + ord(s[i])) % self._prime
        return hash_value

    def _update_hash_simple(self, current_hash, old_char, new_char):
        current_hash = (current_hash - ord(old_char)) % self._prime
        current_hash = (current_hash + ord(new_char)) % self._prime
        return current_hash

    @staticmethod
    def _xor_hash_function(s, length):
        hash_value = 0
        for i in range(length):
            hash_value ^= ord(s[i])
        return hash_value

    @staticmethod
    def _update_hash_xor(current_hash, old_char, new_char):
        current_hash ^= ord(old_char)
        current_hash ^= ord(new_char)
        return current_hash

    def rabin_karp_search(self, text, pattern, hash_type):
        n, m = len(text), len(pattern)
        if n < m:
            return -1

        if hash_type == 'polynomial':
            hash_function = self._polynomial_hash_function
            update_function = self._update_hash_polynomial
        elif hash_type == 'simple':
            hash_function = self._simple_hash_function
            update_function = self._update_hash_simple
        elif hash_type == 'xor':
            hash_function = self._xor_hash_function
            update_function = self._update_hash_xor
        else:
            raise ValueError()

        hash_pattern = hash_function(pattern, m)
        hash_text = hash_function(text, m)

        hash_value = 1
        for i in range(m - 1):
            hash_value = (hash_value * self._alphabet_len) % self._prime

        for i in range(n - m + 1):
            if hash_pattern == hash_text:
                if text[i:i + m] == pattern:
                    return i

            if i + m < n:
                if hash_type in ['simple', 'xor']:
                    hash_text = update_function(hash_text, text[i], text[i + m])
                else:
                    hash_text = update_function(hash_text, text[i], text[i + m], hash_value)

        return -1