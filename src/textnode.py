from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
            )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.NORMAL:
                return LeafNode(self.text)
            case TextType.BOLD:
                return LeafNode(self.text, "b")
            case TextType.ITALIC:
                return LeafNode(self.text, "i")
            case TextType.CODE:
                return LeafNode(self.text, "code")
            case TextType.LINK:
                props = {"href":self.url}
                return LeafNode(self.text, "a", props=props)
            case TextType.IMAGE:
                props = {
                    "src":self.url,
                    "alt":self.text
                    }
                return LeafNode("", "img", props=props)
            case _:
                raise Exception("invalid text type")
            
