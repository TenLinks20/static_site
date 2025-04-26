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
            