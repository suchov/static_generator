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


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_raw_text(self):
        text_node = TextNode("Plain text", TextType.TEXT)
        html_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Plain text")

    def test_text_node_to_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_text_node_to_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_text_node_to_code(self):
        text_node = TextNode("Code snipet", TextType.CODE)
        html_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code snipet</code>")

    def test_text_node_to_link(self):
        text_node = TextNode("Boot.dev", TextType.LINK, url="https://www.boot.dev")
        html_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">Boot.dev</a>')

    def test_text_node_to_image(self):
        text_node = TextNode("Alt text", TextType.IMAGE, url="https://example.com/image.png")
        html_node = TextNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "Alt text"})

    def test_text_node_missing_url(self):
        text_node = TextNode("Alt text", TextType.IMAGE)
        with self.assertRaises(ValueError):
            TextNode.text_node_to_html_node(text_node)

    def test_text_node_unsupported_type(self):
        class UnsupportedType:
            pass

        text_node = TextNode("unsupported", UnsupportedType)
        with self.assertRaises(Exception):
            TextNode.text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()
