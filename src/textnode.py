from htmlnode import LeafNode
from enum import Enum


class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    CODE = "code"
    ITALIC = "italic"
    LINK = "link"
    IMAGE = "image"
    TEXT = "text"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD:
                return LeafNode("b", text_node.text)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text)
            case TextType.CODE:
                return LeafNode("code", text_node.text)
            case TextType.LINK:
                if not text_node.url:
                    raise ValueError("TextNode of type LINK must have a URL.")
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case TextType.IMAGE:
                if not text_node.url:
                    raise ValueError("TextNode of type IMAGE must have a URL.")
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            case _:
                raise Exception(f"Unsupported TextType: {text_node.text_type}")
