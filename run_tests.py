import os
import argparse
import sys
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

from tests.performance_tests.test_time import TimeTester
from tests.performance_tests.test_memory import MemoryTester
from graphics.time_graphic import TimeResultsPlotter
from graphics.memory_graphic import MemoryResultsPlotter
from data_generator import DataGenerator


def main(sizes, pattern, batch_mode):
    generator = DataGenerator(pattern)
    generator.generate_and_save_data(sizes)

    time_tester = TimeTester(sizes, pattern)
    time_tester.run_tests()
    time_tester.save_results()

    time_plotter = TimeResultsPlotter()
    time_plotter.read_data()
    time_plotter.plot_results(batch_mode=batch_mode)

    if batch_mode:
        plt.show()

    memory_tester = MemoryTester(sizes, pattern)
    memory_tester.run_tests()
    memory_tester.save_results()

    memory_plotter = MemoryResultsPlotter()
    memory_plotter.read_data()
    memory_plotter.plot_results(batch_mode=batch_mode)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Инструмент для тестирования производительности '
                    'обработки данных. '
    )
    parser.add_argument(
        '--sizes', type=int, nargs='+',
        default=[1024, 10240, 102400, 1048576, 10485760],
        help='Список размеров данных для тестирования в байтах. '
             'По умолчанию используются размеры: '
             '[1024, 10240, 102400, 1048576, 10485760]. '
             'Вы можете указать несколько значений, разделённых '
             'пробелами без скобок.'
    )
    parser.add_argument(
        '--pattern', type=str, default='pattern',
        help='Шаблон, используемый для генерации данных. '
             'По умолчанию используется шаблон "pattern". '
             'Вы можете указать свой собственный шаблон, '
             'указав без кавычек.'
    )
    parser.add_argument(
        '--batch', action='store_true',
        help='Запуск в пакетном режиме. '
             'При активации этого параметра результаты будут '
             'отображены только после завершения всех тестов.'
    )

    args = parser.parse_args()
    if args.batch:
        print("Запуск в пакетном режиме...")

    main(args.sizes, args.pattern, args.batch)
