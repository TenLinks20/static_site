import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
        self.assertIsInstance(node.props_to_html(), str)        
    
    def test_props_value_error(self):
        node = HTMLNode(props=None)
        with self.assertRaises(ValueError) as context:
            node.props_to_html()
        
        self.assertEqual(str(context.exception), "props attribute is None")



    def test_leaf_to_html_p(self):
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("Hello, world!", "a", {"key": "val"})
        self.assertEqual(node.to_html(), '<a key="val">Hello, world!</a>')

    def test_leaf_value_error(self):
        node = LeafNode(None, "a", {"key":"val"})
        with self.assertRaises(ValueError) as context:
            node.to_html()
        
        self.assertEqual(str(context.exception), "value attribute is None")

    

    def test_to_html_with_children(self):
        child_node = LeafNode("child", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
