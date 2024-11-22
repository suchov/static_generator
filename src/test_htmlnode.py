import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="p", value="This is a paragraph.")
        expected_repr = "HTMLNode(tag=p, value=This is a paragraph., children=0 children, props={})"
        self.assertEqual(repr(node), expected_repr)

    def test_complex_node(self):
        child_node = HTMLNode(tag="span", value="This is a span.")
        parent_node = HTMLNode(tag="div", children=[child_node], props={"class": "container"})

        # Check props_to_html for parent node
        self.assertEqual(parent_node.props_to_html(), ' class="container"')
        # Ensure the parent node has one child
        self.assertEqual(len(parent_node.children), 1)
        # Check child node's tag
        self.assertEqual(parent_node.children[0].tag, "span")
        # Check child node's value
        self.assertEqual(parent_node.children[0].value, "This is a span.")


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_raw_text(self):
        text_node = TextNode("Plain text", TextType.TEXT)
        html_node = HTMLNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Plain text")

    def test_text_node_to_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = HTMLNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_text_node_to_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = HTMLNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_text_node_to_code(self):
        text_node = TextNode("Code snipet", TextType.CODE)
        html_node = HTMLNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code snipet</code>")

    def test_text_node_to_link(self):
        text_node = TextNode("Boot.dev", TextType.LINK, url="https://www.boot.dev")
        html_node = HTMLNode.text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev">Boot.dev</a>')

#    def test_text_node_to_image(self):
#        text_node = TextNode("Alt text", TextType.IMAGE, url="https://example.com/image.png")
#        html_node = HTMLNode.text_node_to_html_node(text_node)
#        self.assertEqual(html_node.to_html(), '<img src="https://example.com/image.png" alt="Alt text">')

    def test_text_node_missing_url(self):
        text_node = TextNode("Alt text", TextType.IMAGE)
        with self.assertRaises(ValueError):
            HTMLNode.text_node_to_html_node(text_node)

    def test_text_node_unsupported_type(self):
        class UnsupportedType:
            pass

        text_node = TextNode("unsupported", UnsupportedType)
        with self.assertRaises(Exception):
            HTMLNode.text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()
