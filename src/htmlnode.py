class HTMLNode:
    
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # Child classes will override this method to render themselvs at HTML
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is None:
            raise ValueError("props attribute is None")
        # Converts dict of HTML attributes to valid HTML formatting
        props_list = [f'{k}="{v}"' for k, v in self.props.items()]
        props_text = " ".join(props_list)
        return props_text
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
            

class LeafNode(HTMLNode):

    def __init__(self, value: str, tag: str = None, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("value attribute is None")
        if self.tag is None:
            return self.value
        elif self.props is not None:
            props_text = super().props_to_html()
            return f"<{self.tag} {props_text}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.value}, {self.tag}, {self.props})"
        

class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: list[HTMLNode], props: dict = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag attribute is None")
        if self.children is None:
            raise ValueError("children attribute is None")
        else:
            text = "".join(child.to_html() for child in self.children)
            return f"<{self.tag}>{text}</{self.tag}>"

            
        
