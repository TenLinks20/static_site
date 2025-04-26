import unittest
from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()
