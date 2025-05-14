class ZFunctionSearch():

    @staticmethod
    def find_z_function(text):
        z = [0] * len(text)
        l, r, n = 0, 0, len(text)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and text[z[i]] == text[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z

    def z_function_search(self, text, pattern):
        concat = pattern + '$' + text
        z = self.find_z_function(concat)

        pattern_length = len(pattern)
        for i in range(len(z)):
            if z[i] == pattern_length:
                return i - pattern_length - 1

        return -1