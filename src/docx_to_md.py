# Convert docx to markdown
import mammoth

input_docx = "data/raw/projects.docx"
output_md = "data/raw/projects.md"

# Open the DOCX file for reading
with open(input_docx, "rb") as docx_file:
    # Convert the DOCX file to markdown
    result = mammoth.convert_to_markdown(docx_file)

# Open the markdown file for writing
with open(output_md, "w") as markdown_file:
    # Write the converted markdown content to the markdown file
    markdown_file.write(result.value)

print(f"Markdown file created at {output_md}")