from textnode import TextNode, TextType


    
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


    