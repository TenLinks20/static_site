from textnode import TextNode, TextType

def main():
    test_node = TextNode("I'm in the main() function", TextType.LINK, "https://example.com")
    print(test_node)

main()
