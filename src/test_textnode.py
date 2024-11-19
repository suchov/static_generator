import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_blank_link(self):
        node = TextNode("This is a link", TextType.LINK)
        node2 = TextNode("This is a link", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a link", TextType.LINK)
        node2 = TextNode("This is a linkis", TextType.LINK, None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
