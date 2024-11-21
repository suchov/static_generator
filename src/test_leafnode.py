import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_render_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click me!</a>')

    def test_render_with_tag_no_props(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_render_raw_text(self):
        node = LeafNode(None, "Just raw text.")
        self.assertEqual(node.to_html(), "Just raw text.")

    def test_missing_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_render_empty_value_raises_error(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
