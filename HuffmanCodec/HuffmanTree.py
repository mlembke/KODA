from collections import Counter


class HuffmanNode(object):
    def __init__(self, symbol=None, frequency=0, left=None, right=None, parent=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return '({0}, {1})'.format(self.symbol, self.frequency)

    def __eq__(self, other):
        if isinstance(other, HuffmanNode):
            return self.frequency == other.frequency
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, HuffmanNode):
            return self.frequency >= other.frequency
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, HuffmanNode):
            return self.frequency <= other.frequency
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, HuffmanNode):
            return self.frequency > other.frequency
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, HuffmanNode):
            return self.frequency < other.frequency
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is not NotImplemented:
            return not result
        return NotImplemented


class HuffmanTree(object):
    def __init__(self, root=None):
        self.root = root

    def generate_code_book(self):
        code_book = {}
        _generate_huffman_code(self.root, code_book)
        return code_book


def build_tree(data):
    frequencies = Counter(data)
    nodes = [HuffmanNode(symbol, frequency) for symbol, frequency in frequencies.items()]
    return HuffmanTree(_build_tree(nodes))


def _build_tree(nodes):
    nodes.sort()
    while True:
        first, second = _pop_front_two_nodes(nodes)
        if not second:
            return first
        parent = HuffmanNode(frequency=first.frequency + second.frequency, left=first, right=second)
        first.parent = parent
        second.parent = parent
        nodes.insert(0, parent)
        nodes.sort()


def _pop_front_two_nodes(nodes):
    if len(nodes) > 1:
        first = nodes.pop(0)
        second = nodes.pop(0)
        return first, second
    elif len(nodes) == 1:
        return nodes.pop(0), None
    return None, None


def _generate_huffman_code(node, code_book, code=[]):
    if not node.left and not node.right:
        code_book[node.symbol] = ''.join(code)
        return
    code.append('0')
    _generate_huffman_code(node.left, code_book, code)
    code.pop()

    code.append('1')
    _generate_huffman_code(node.right, code_book, code)
    code.pop()
