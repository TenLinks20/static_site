import os
import shutil
from textnode import TextNode, TextType


def cp_all_to_dir(src_dir:str, dst_dir:str, is_top_level:bool=True):
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
                cp_all_to_dir(current_path, dst_path, False)
    else:
        shutil.copy(src_dir, dst_dir)
    return
        
        
    

def main():
    test_node = TextNode("I'm in the main() function", TextType.LINK, "https://example.com")
    print(test_node)
    cp_all_to_dir("static", "public")
    

main()
