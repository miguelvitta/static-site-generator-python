from enum import Enum
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_html_node(markdown):
    # 1. Split markdown into blocks using markdown_to_blocks
    # 2. For each block, call block_to_html_node and collect results
    # 3. Return a ParentNode with tag "div" wrapping all block nodes
    pass


def block_to_html_node(block):
    # 1. Determine the block type using block_to_block_type
    # 2. Call the appropriate handler function based on the type
    # 3. Raise a ValueError if the block type is unrecognized
    pass


def text_to_children(text):
    # 1. Call text_to_textnodes(text) to get a list of TextNodes
    # 2. Convert each TextNode to an HTMLNode using text_node_to_html_node
    # 3. Return the list of HTMLNodes
    pass


def paragraph_to_html_node(block):
    # 1. Split the block into lines
    # 2. Join the lines with a space (removes newlines inside a paragraph)
    # 3. Call text_to_children on the joined text
    # 4. Return a ParentNode with tag "p" and those children
    pass


def heading_to_html_node(block):
    # 1. Count the number of leading "#" characters — that's the heading level
    # 2. Strip the "# " prefix to get the heading text
    # 3. Call text_to_children on the text
    # 4. Return a ParentNode with tag f"h{level}"
    pass


def code_to_html_node(block):
    # 1. Strip the opening and closing ``` markers to get the raw text
    # 2. Do NOT use text_to_children here — no inline markdown parsing
    # 3. Manually create a TextNode with TextType.TEXT and convert it
    # 4. Wrap it in a ParentNode("code", ...) then wrap that in ParentNode("pre", ...)
    pass


def quote_to_html_node(block):
    # 1. Split into lines
    # 2. Strip the leading ">" (and optional space) from each line
    # 3. Join the lines back together
    # 4. Call text_to_children on the content
    # 5. Return a ParentNode with tag "blockquote"
    pass


def ulist_to_html_node(block):
    # 1. Split the block into lines
    # 2. For each line, strip the leading "- " to get the item text
    # 3. Call text_to_children on each item text
    # 4. Wrap each in a ParentNode("li", ...)
    # 5. Return a ParentNode("ul", ...) containing all the <li> nodes
    pass


def olist_to_html_node(block):
    # 1. Split the block into lines
    # 2. For each line, strip the "N. " prefix to get the item text
    #    (hint: split on ". " with maxsplit=1 and take the second part)
    # 3. Call text_to_children on each item text
    # 4. Wrap each in a ParentNode("li", ...)
    # 5. Return a ParentNode("ol", ...) containing all the <li> nodes
    pass


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned = []
    for block in blocks:
        block = block.strip()
        if block != "":
            cleaned.append(block)
    return cleaned


def block_to_block_type(block):
    if block.startswith("#"):
        i = 0
        while i < len(block) and block[i] == "#":
            i += 1
        if 1 <= i <= 6 and i < len(block) and block[i] == " ":
            return BlockType.HEADING

    lines = block.split("\n")

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
