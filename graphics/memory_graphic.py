import matplotlib.pyplot as plt
import os


class MemoryResultsPlotter:

    def __init__(self, filename='memory_result.txt'):
        self.filename = filename
        self.results = {
            'Brute-Force': {'best': [], 'random': [], 'worst': []},
            'Rabin-Karp': {'best': [], 'random': [], 'worst': []},
            'KMP': {'best': [], 'random': [], 'worst': []},
            'Aho-Corasick': {'best': [], 'random': [], 'worst': []},
            'Z-function': {'best': [], 'random': [], 'worst': []}
        }
        self.sizes = []

    def read_data(self):
        results_dir = os.path.join('result')
        file_path = os.path.join(results_dir, self.filename)

        with open(file_path, 'r') as file:
            next(file)
            for line in file:
                data_type, size, algotithm, usage_memory = line.split()
                size = int(size)
                usage_memory = float(usage_memory)

                if algotithm in self.results:
                    self.results[algotithm][data_type].append((size, usage_memory))
                    if size not in self.sizes:
                        self.sizes.append(size)

    def plot_results(self, batch_mode=False):
        plt.figure(figsize=(12, 8))

        for algorithm, data_types in self.results.items():
            for data_type, size_memory in data_types.items():
                size, memory = zip(*size_memory) if size_memory else ([], [])
                plt.plot(size, memory, marker='o', label=f'{algorithm} - {data_type}')

        plt.xscale('log')
        plt.yscale('log')
        plt.title('Использованная память по типу данных')
        plt.xlabel('Размер данных (байты)')
        plt.ylabel('Память (байты)')
        plt.legend()
        plt.grid(True, which="both", linestyle='--', linewidth=0.5)
        plt.xticks(self.sizes, rotation=45)
        plt.tight_layout()

        image_dir = os.path.join('result_images')
        os.makedirs(image_dir, exist_ok=True)

        plt.savefig(os.path.join(image_dir, 'memory_result_plot.png'))

        if batch_mode:
            plt.show()
