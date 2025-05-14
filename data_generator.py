import random
import string
import os


class DataGenerator:
    def __init__(self, pattern):
        self._pattern = pattern

    def generate_data(self, size):
        all_characters = (
            string.ascii_letters + string.digits + string.punctuation + ' '
        )
        return ''.join(random.choices(all_characters, k=size))

    def generate_random_data(self, size):
        if size < len(self._pattern):
            raise ValueError(
                'Размер строки должен быть больше или равен размеру шаблона'
            )

        random_data_size = size - len(self._pattern)
        random_data_part = self.generate_data(random_data_size)
        insert_position = random.randint(0, random_data_size)
        result = (
            random_data_part[:insert_position] + self._pattern +
            random_data_part[insert_position:]
        )

        return result

    def generate_best_data(self, size):
        return self._pattern + self.generate_data(size - len(self._pattern))

    def generate_worst_data(self, size):
        return (
            self.generate_data(size - len(self._pattern)) + self._pattern
        )

    def save_data_to_file(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)

    def generate_and_save_data(self, sizes):
        os.makedirs('data', exist_ok=True)

        for size in sizes:
            random_data = self.generate_random_data(size)
            best_data = self.generate_best_data(size)
            worst_data = self.generate_worst_data(size)

            self.save_data_to_file(f"data/random_{size}.txt", random_data)
            self.save_data_to_file(f"data/best_{size}.txt", best_data)
            self.save_data_to_file(f"data/worst_{size}.txt", worst_data)
