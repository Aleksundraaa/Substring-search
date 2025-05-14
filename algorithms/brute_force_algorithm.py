class BruteForceSearch:
    @staticmethod
    def brute_force_search(text, pattern):
        n, m = len(text), len(pattern)
        if n < m:
            return -1
        for i in range(n - m + 1):
            if text[i:i + m] == pattern:
                return i
        return -1