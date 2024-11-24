from textnode import TextNode, TextType
from split_nodes import extract_markdown_links, extract_markdown_images


def split_nodes_image(old_nodes):
    """
    Split text nodes into a list of nodes based on markdown images.
    :param old_nodes: List of TextNode objects.
    :return: List of TextNode objects with images extracted.
    """
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Keep non-text nodes as-is
            new_nodes.append(node)
            continue

        # Extract images from the node's text
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)  # No images, keep the original node
            continue

        # Process each image
        text = node.text
        for alt_text, url in images:
            sections = text.split(f"![{alt_text}]({url})", 1)
            if sections[0]:  # Add preceding text if not empty
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            text = sections[1] if len(sections) > 1 else ""

        if text:  # Add remaining text if not empty
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    """
    Split text nodes into a list of nodes based on markdown links.
    :param old_nodes: List of TextNode objects.
    :return: List of TextNode objects with links extracted.
    """
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Keep non-text nodes as-is
            new_nodes.append(node)
            continue

        # Extract links from the node's text
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)  # No links, keep the original node
            continue

        # Process each link
        text = node.text
        for anchor_text, url in links:
            sections = text.split(f"[{anchor_text}]({url})", 1)
            if sections[0]:  # Add preceding text if not empty
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            text = sections[1] if len(sections) > 1 else ""

        if text:  # Add remaining text if not empty
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
