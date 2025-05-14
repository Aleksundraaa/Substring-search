import os
from memory_profiler import memory_usage
from algorithms.brute_force_algorithm import BruteForceSearch
from algorithms.rabin_karp_algorithm import RabinKarpSearch
from algorithms.knuth_morris_pratt import KMPSearch
from algorithms.aho_corasick_algorithm import AhoCorasickSearch
from algorithms.z_function_algorithm import ZFunctionSearch

class MemoryTester:
    def __init__(self, sizes, pattern):
        self._sizes = sizes
        self._pattern = pattern
        self._brute_force = BruteForceSearch()
        self._rabin_karp = RabinKarpSearch()
        self._kmp = KMPSearch()
        self._aho_corasick = AhoCorasickSearch([self._pattern])
        self._z_function = ZFunctionSearch()
        self._memory_result = []

    @staticmethod
    def _measure_memory(algorithm, text, *args):
        def wrapped_algorithm():
            return algorithm(text, *args)

        mem_usage = memory_usage(wrapped_algorithm)
        return max(mem_usage)

    def run_tests(self):
        for size in self._sizes:
            for data_type in ['best', 'random', 'worst']:
                file_path = os.path.join('data', f'{data_type}_{size}.txt')
                try:
                    with open(file_path, 'r') as file:
                        text = file.read()

                    brute_force_memory = self._measure_memory(self._brute_force.brute_force_search, text, self._pattern)
                    self._memory_result.append((data_type, size, 'Brute-Force', brute_force_memory))

                    hash_type = 'polynomial'
                    rabin_karp_memory = self._measure_memory(self._rabin_karp.rabin_karp_search, text, self._pattern, hash_type)
                    self._memory_result.append((data_type, size, 'Rabin-Karp', rabin_karp_memory))

                    kmp_memory = self._measure_memory(self._kmp.kmp_search, text, self._pattern)
                    self._memory_result.append((data_type, size, 'KMP', kmp_memory))

                    aho_corasick_memory = self._measure_memory(self._aho_corasick.aho_corasick_search, text, self._pattern)
                    self._memory_result.append((data_type, size, 'Aho-Corasick', aho_corasick_memory))

                    z_function_memory = self._measure_memory(self._z_function.z_function_search, text, self._pattern)
                    self._memory_result.append((data_type, size, 'Z-function', z_function_memory))

                except FileNotFoundError:
                    print(f"Файл не найден: {file_path}. Пропуск теста.")
                except Exception as e:
                    print(f"Ошибка при обработке файла {file_path}: {e}")

    def save_results(self, filename='memory_result.txt'):
        results_dir = os.path.join('.', 'result')
        os.makedirs(results_dir, exist_ok=True)
        file_path = os.path.join(results_dir, filename)
        with open(file_path, 'w', newline='') as file:
            file.write('Data Type     Size(byte)    Algorithm         Memory(byte)\n')
            for result in self._memory_result:
                line = f'{result[0]:<13} {result[1]:<13} {result[2]:<17} {result[3]}\n'
                file.write(line)
