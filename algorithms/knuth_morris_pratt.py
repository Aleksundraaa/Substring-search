class KMPSearch:
    @staticmethod
    def prefix(pattern):
        '''
        составляем массив частичных совпадений, чтобы избежать повторных сравнений
        '''
        m = len(pattern)
        prefix_function = [0] * m
        g = 0
        for i in range(1, m):
            while g > 0 and pattern[i] != pattern[g]:
                g = prefix_function[g - 1]
            if pattern[i] == pattern[g]:
                g += 1
            prefix_function[i] = g
        return prefix_function

    def kmp_search(self, text, pattern):
        if not pattern:
            return 0

        index = -1
        f = self.prefix(pattern)
        k = 0

        for i in range(len(text)):
            while k > 0 and pattern[k] != text[i]:
                k = f[k - 1]
            if pattern[k] == text[i]:
                k += 1
            if k == len(pattern):
                index = i - len(pattern) + 1
                break

        return index
