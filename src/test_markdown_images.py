import unittest
from split_nodes import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_extract_markdown_imagess(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(result, expected)

    def test_extract_markdown_linkss(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(result, expected)

    def test_no_images(self):
        text = "This is text with no images."
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_no_links(self):
        text = "This is text with no links."
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_images_and_links_mixed(self):
        text = (
            "Here is an image ![alt text](https://example.com/image.png) and a link [to site](https://example.com)."
        )
        images = extract_markdown_images(text)
        links = extract_markdown_links(text)
        self.assertEqual(images, [("alt text", "https://example.com/image.png")])
        self.assertEqual(links, [("to site", "https://example.com")])


if __name__ == "__main__":
    unittest.main()
