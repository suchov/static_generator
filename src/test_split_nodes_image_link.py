import unittest
from textnode import TextNode, TextType
from split_nodes_images_markdown import split_nodes_image, split_nodes_link


class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_image(self):
        text = "This is text with an image ![alt](https://example.com/image.png) and more text."
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and more text.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is text with no images.", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

    def test_split_nodes_link(self):
        text = "Here is a link [to example](https://example.com) and another [to google](https://google.com)."
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
                TextNode("Here is a link ", TextType.TEXT),
                TextNode("to example", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://google.com"),
                TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_no_links(self):
        node = TextNode("This is text with no links.", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [node])

    def test_mixed_nodes(self):
        text = "Here is a link [to example](https://example.com) and an image ![alt](https://example.com/image.png)."
        node = TextNode(text, TextType.TEXT)
        link_nodes = split_nodes_link([node])
        image_nodes = split_nodes_image(link_nodes)
        expected = [
            TextNode("Here is a link ", TextType.TEXT),
            TextNode("to example", TextType.LINK, "https://example.com"),
            TextNode(" and an image ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(image_nodes, expected)


if __name__ == "__main__":
    unittest.main()
