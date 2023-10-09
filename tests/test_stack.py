"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import *

class TestStack(unittest.TestCase):
    n1 = Node(5, None)
    n2 = Node('a', n1)

    def test_node(self):
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, "a")
        self.assertEqual(self.n1, self.n2.next_node)


    def test_stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, "data3")
        self.assertEqual(stack.top.next_node.data, "data2")
        self.assertEqual(stack.top.next_node.next_node.data, "data1")
        self.assertEqual(stack.top.next_node.next_node.next_node, None)