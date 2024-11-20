import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
