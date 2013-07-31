import random
from tree import Tree, BinarySearchTree

def test_tree():
    t = Tree.from_list([
        'a', 1, [
            ['b', 2, [
                ['d', 4, [
                    ['f', 5, [
                    ]]
                ]]
            ]],
            ['c', 3, [
            ]],
            ['e', 5, [
            ]]
    ]])
    assert t.dfs('e') == 5
    assert t.dfs('d') == 4
    assert t.dfs_recursive(t.root, 'd') == 4
    assert t.dfs_recursive(t.root, 'e') == 5
    assert t.bfs('d') == 4
    assert t.bfs('e') == 5


def test_BST():
    t = BinarySearchTree()
    data = list(range(100))
    random.shuffle(data)
    for val in data:
        t.insert(val, val ** 2)
    for val in range(100):
        assert t.find(val) == val ** 2
        assert t.find_recursive(t.root, val) == val ** 2
    assert t.min() == 0
    assert t.max() == 99