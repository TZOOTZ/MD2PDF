# MD2PDF

Convert Markdown files to beautifully formatted PDFs with classic novel styling.

## Overview

MD2PDF is a powerful command-line tool that automatically converts Markdown files to PDF format, applying classic novel-style formatting. Whether you're working with single files or entire directories, MD2PDF handles the conversion process while maintaining professional formatting and structure.

## Key Features

- Automated processing of single files or complete directories
- Automatic generation of:
  - Page numbers
  - Styled headers
  - Justified text with indentation
  - Custom footers
- Full support for:
  - Tables (with borders)
  - Code blocks (with syntax highlighting)
  - Hyperlinks
- Option to merge multiple PDFs into a single document

## Technical Requirements

### System Requirements
- Python 3.9 or higher
- Required fonts:
  - Garamond
  - Times New Roman

### Dependencies
```
weasyprint >= 54.0
PyPDF2 >= 3.0.0
markdown >= 3.3.7
```

## Technical Specifications

### Input/Output
- Input: `.md` files or directory containing `.md` files
- Output: PDF file(s) in specified directory

### Processing Pipeline
1. Markdown to HTML conversion
2. CSS styling application
3. PDF rendering
4. Optional: PDF merging

## Command Line Options

```
md2pdf [options] <input>

Options:
--output    Output directory (default: pdf_output)
--css       Custom CSS file (default: classic_book.css)
--merge     Combine all PDFs into merged.pdf
```

## Technical Notes

- Fixed positioning is used for footers to ensure they appear on all pages
- Code blocks implement horizontal scrolling using `overflow-x: auto`
- Markdown conversion includes extensions for:
  - Tables
  - Fenced code blocks

## Installation

```bash
pip install md2pdf
```

## Development

MD2PDF is developed and maintained by TZOOTZ RESEARCH.

## License

[License information to be added]

## Contributing

[Contributing guidelines to be added]
