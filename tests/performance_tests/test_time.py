import time
import os
from algorithms.brute_force_algorithm import BruteForceSearch
from algorithms.rabin_karp_algorithm import RabinKarpSearch
from algorithms.knuth_morris_pratt import KMPSearch
from algorithms.aho_corasick_algorithm import AhoCorasickSearch
from algorithms.z_function_algorithm import ZFunctionSearch


class TimeTester:
    def __init__(self, sizes, pattern):
        self._sizes = sizes
        self._pattern = pattern
        self._brute_force = BruteForceSearch()
        self._rabin_karp = RabinKarpSearch()
        self._kmp = KMPSearch()
        self._aho_corasick = AhoCorasickSearch([self._pattern])
        self._z_function = ZFunctionSearch()
        self._time_results = []

    @staticmethod
    def _measure_time(algorithm, text, *args):
        start_time = time.perf_counter()
        algorithm(text, *args)
        end_time = time.perf_counter()
        return end_time - start_time

    def run_tests(self):
        for size in self._sizes:
            for data_type in ['best', 'random', 'worst']:
                file_path = os.path.join('data', f'{data_type}_{size}.txt')
                with open(file_path, 'r') as file:
                    text = file.read()

                brute_force_time = self._measure_time(self._brute_force.brute_force_search, text, self._pattern)
                self._time_results.append((data_type, size, 'Brute-Force', brute_force_time))

                hash_type = 'polynomial'
                rabin_karp_time = self._measure_time(self._rabin_karp.rabin_karp_search, text, self._pattern, hash_type)
                self._time_results.append((data_type, size, 'Rabin-Karp', rabin_karp_time))

                kmp_time = self._measure_time(self._kmp.kmp_search, text, self._pattern)
                self._time_results.append((data_type, size, 'KMP', kmp_time))

                aho_corasick_time = self._measure_time(self._aho_corasick.aho_corasick_search, text, self._pattern)
                self._time_results.append((data_type, size, 'Aho-Corasick', aho_corasick_time))

                z_function_time = self._measure_time(self._z_function.z_function_search, text, self._pattern)
                self._time_results.append((data_type, size, 'Z-function', z_function_time))

    def save_results(self, filename='time_result.txt'):
        results_dir = os.path.join('.', 'result')
        os.makedirs(results_dir, exist_ok=True)
        file_path = os.path.join(results_dir, filename)

        with open(file_path, 'w', newline='') as file:
            file.write('Data Type     Size(byte)    Algorithm         Execution Time(ms)\n')
            for result in self._time_results:
                line = f'{result[0]:<13} {result[1]:<13} {result[2]:<17} {result[3] * 1000}\n'
                file.write(line)
