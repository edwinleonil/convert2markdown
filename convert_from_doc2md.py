from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)  # Set to True to enable plugins
result = md.convert(r"C:\Users\me1elar\Downloads\sow.docx")

# Access the markdown content from the result object
# Use one of these approaches based on the library's API:
# Option 1:
markdown_content = result.markdown

# Option 2 (if the above doesn't work):
# markdown_content = str(result)

# save the result as md file
with open("sow.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)
