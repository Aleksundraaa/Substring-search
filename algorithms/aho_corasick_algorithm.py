class Node:
    def __init__(self):
        self.goto = {}  # Словарь переходов для символов
        self.out = []  # Список шаблонов, соответствующих этому узлу
        self.fail = None  # Указатель на узел неудачи


class AhoCorasickSearch:
    def __init__(self, patterns):
        self.root = self._create_forest(patterns)
        self._create_statemachine()

    @staticmethod
    def _create_forest(patterns):
        '''
        Создаем дерево узлов для заданных шаблонов.
        Получаем root - корневой узел дерева
        '''
        root = Node()
        for path in patterns:
            node = root
            for symbol in path:
                node = node.goto.setdefault(symbol, Node())
            node.out.append(path)
        return root

    def _create_statemachine(self):
        '''
        Создаем автомат состояний для алгоритма
        '''
        queue = []
        for node in self.root.goto.values():
            queue.append(node)
            node.fail = self.root

        while queue:
            rnode = queue.pop(0)

            for key, unode in rnode.goto.items():
                queue.append(unode)
                fnode = rnode.fail
                while fnode is not None and key not in fnode.goto:
                    fnode = fnode.fail
                unode.fail = fnode.goto[key] if fnode else self.root
                unode.out += unode.fail.out

    def aho_corasick_search(self, text, pattern):
        if pattern == "":
            return 0

        node = self.root
        for i in range(len(text)):
            while node is not None and text[i] not in node.goto:
                node = node.fail
            if node is None:
                node = self.root
                continue
            node = node.goto[text[i]]
            if pattern in node.out:
                return i - len(pattern) + 1

        return -1