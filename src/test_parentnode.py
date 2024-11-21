import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):

    def test_render_simple_parent_node(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                ],
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i></p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_missing_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")])

    def test_missing_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_nested_parent_nodes(self):
        child = ParentNode(
                "ul",
                [
                    LeafNode("li", "Item 1"),
                    LeafNode("li", "Item 2"),
                ],
        )
        parent = ParentNode(
                "div",
                [
                    LeafNode("h1", "Header"),
                    child,
                ],
        )
        expected_html = "<div><h1>Header</h1><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_props_on_parent_node(self):
        node = ParentNode(
                "div",
                [LeafNode("span", "Content")],
                props={"class": "container", "id": "main-div"},
        )
        expected_html = '<div class="container" id="main-div"><span>Content</span></div>'
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
