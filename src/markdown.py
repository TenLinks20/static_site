from textnode import TextNode, TextType
import re


    
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        split_texts = node.text.split(delimiter)

        if len(split_texts) % 2 == 0:
            raise ValueError(f"Invalid markdown: unmatched '{delimiter}' delimiter in '{node.text}'")

        for i, piece in enumerate(split_texts):
            if piece == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(piece, TextType.NORMAL))
            else:
                new_nodes.append(TextNode(piece, text_type))

    return new_nodes

def extract_markdown_images(text: str) -> list[tuple]:
    extracted_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted_text

def extract_markdown_links(text: str) -> list[tuple]:
    extracted_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted_text

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text_to_process = node.text 
        images = extract_markdown_images(text_to_process)

        if not images:
            new_nodes.append(node)
            continue

        for img_alt, img_url in images:
            delimiter = f"![{img_alt}]({img_url})"
            parts = text_to_process.split(delimiter, 1)

            if len(parts) != 2:
                raise ValueError(f"Invalid markdown: unmatched image delimiter '{delimiter}'")

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))

            new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_url))
            text_to_process = parts[1]

        if text_to_process:
            new_nodes.append(TextNode(text_to_process, TextType.NORMAL))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text_to_process = node.text
        links = extract_markdown_links(text_to_process)

        if not links:
            new_nodes.append(node)
            continue

        for link_text, link_url in links:
            delimiter = f"[{link_text}]({link_url})"
            parts = text_to_process.split(delimiter, 1)

            if len(parts) != 2:
                raise ValueError(f"Invalid markdown: unmatched link delimiter '{delimiter}'")

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            text_to_process = parts[1]

        if text_to_process:
            new_nodes.append(TextNode(text_to_process, TextType.NORMAL))

    return new_nodes

    