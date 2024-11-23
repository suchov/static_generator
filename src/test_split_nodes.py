import unittest
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDeliviter(unittest.TestCase):

    def test_plain_text_no_delimiter(self):
        node = TextNode("This is plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [node])

    def test_single_bold_phrase(self):
        node = TextNode("This is **bold text** in a sentence", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in a sentence", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_bold_phrases(self):
        node = TextNode("**Bold1** and **Bold2**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Bold1", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("Bold2", TextType.BOLD),
        ]
        self.assertEqual(expected, result)

    def test_inline_code(self):
        node = TextNode("Here is `inline code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("inline code", TextType.CODE),
        ]
        self.assertEqual(result, expected)

    def test_nested_delimeter(self):
        node = TextNode("This is **bold and *italic*** text", TextType.TEXT)
        bold_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        # expected = [
        #    TextNode("This is ", TextType.TEXT),
        #    TextNode("bold and ", TextType.BOLD),
        #    TextNode("italic", TextType.ITALIC),
        #    TextNode("", TextType.BOLD),
        #    TextNode(" text", TextType.TEXT),
        # ]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(bold_nodes, "*", TextType.ITALIC)

    def test_unmatched_delimeter(self):
        node = TextNode("This is a **unmatched", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    if __name__ == "main":
        unittest.main()
