import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is the text node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is the text node", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()