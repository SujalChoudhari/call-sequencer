from call_sequencer import CallSequencer
from call_sequencer.markdown_extractors import extract_lists, extract_bold_text,extract_code_blocks

@CallSequencer.simple
def simple_func(param):
    # operation
    return param


@CallSequencer.with_args
def with_args_func(param1, *args):
    # operation
    return "res" + param1 + "".join(args)


def test_main():
    markinput = """


### Using Chains of Functions

```python
from call_sequencer import CallSequencer
# Example Usage
@CallSequencer.simple
def sanitize(param) -> str:...

@CallSequencer.simple
def retrive_data(param)-> str:...

@CallSequencer.with_args
def query_llm(param, *args, **kwargs)-> str:...

@CallSequencer.simple
def extract_code(param)-> str:...

@CallSequencer.simple
def execute_code(param)-> str:...


code_evaluator = (
    CallSequencer.start("Hello")  # Initial input block
    >> sanitize
    >> retrive_data
    >> query_llm("extra_param")
    >> extract_code
    >> execute_code
    >> query_llm("another_param")
)

# Run the chain
result = code_evaluator()
print("Final Result:", result)

```

### Predefined Functions
# Explanation of Markdown Parsing Functions

1. **extract_title**
   - Extracts the title from a Markdown string, identified by a single `#` at the beginning of a line. Returns `None` if no title is found.

2. **extract_code_blocks**
   - Extracts all code blocks from a Markdown string delimited by triple backticks (` ``` `). Returns a list of code block strings.

3. **extract_tables**
   - Extracts tables from a Markdown string formatted with pipes (`|`). Returns a list of table row strings.

4. **extract_lists**
   - Extracts both ordered (numbered) and unordered (bulleted) lists from a Markdown string. Returns a list of list item strings.

5. **extract_first_code_block**
   - Extracts the content of the first code block encountered in a Markdown string. Returns `None` if no code block is found.

6. **extract_headings**
   - Extracts all headings from a Markdown string, identified by lines starting with multiple `#` characters. Returns a list of heading strings.

7. **extract_bold_text**
   - Extracts text formatted in bold (`**text**`) from a Markdown string. Returns a list of bold text strings.

8. **extract_italic_text**
   - Extracts text formatted in italics (`*text*`) from a Markdown string. Returns a list of italic text strings.

9. **extract_links**
   - Extracts hyperlinks in the format `[text](url)` from a Markdown string. Returns a list of tuples where each tuple contains the text and URL.

10. **extract_all_text**
    - Strips out all Markdown formatting (bold, italic, links) and returns plain text from a Markdown string. Returns a plain string of text content.
"""
    seq = CallSequencer.start(markinput) >> extract_code_blocks
    print(seq())

test_main()