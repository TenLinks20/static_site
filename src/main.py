import os
import shutil
from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode
from markdown_blocks import markdown_to_html_node, markdown_to_blocks


def cp_content(src_dir:str, dst_dir:str, is_top_level:bool=True):
    if is_top_level:
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)
        os.mkdir(dst_dir)
    else:
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
    
    if os.path.isdir(src_dir):
        src_subpaths = os.listdir(src_dir)
        for path in src_subpaths:
            current_path = os.path.join(src_dir, path)
            dst_path = os.path.join(dst_dir, path)
            if os.path.isfile(current_path):
                shutil.copy(current_path, dst_path)
                print(f"File: {current_path} was added to {dst_path}")
            else:
                cp_content(current_path, dst_path, False)
    else:
        shutil.copy(src_dir, dst_dir)
    return

def extract_title(markdown: str):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise ValueError("No h1 tag in markdown")

    

def generate_page(from_path:str, template_path: str, dest_path:str):
    print(f"Generating Page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path, "r", encoding="utf-8") as ff:
        md_content = ff.read()
    
    with open(template_path, "r", encoding="utf-8") as tf:
        template_content = tf.read()
    
    node = markdown_to_html_node(md_content)
    content = node.to_html()
    title = extract_title(md_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", content)

    if os.path.dirname(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w", encoding="utf-8") as df:
        df.write(template_content)      
        
    

def main():
    test_node = TextNode("I'm in the main() function", TextType.LINK, "https://example.com")
    print(test_node)
    cp_content("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    
if __name__ == '__main__':
    main()
