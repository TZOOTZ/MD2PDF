# md2pdf.py
import argparse
import os
import sys
import markdown
from pathlib import Path
from PyPDF2 import PdfMerger
from weasyprint import HTML, CSS

def convert_md_to_pdf(input_path, output_dir, css=None, merge=False):
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    md_files = []
    if input_path.is_dir():
        md_files = sorted(input_path.glob("**/*.md"))
    elif input_path.suffix == ".md":
        md_files = [input_path]
    else:
        raise ValueError("Debe ser un archivo .md o directorio con .md")
    
    # CSS por defecto
    if not css:
        css = str(Path(__file__).parent / "styles" / "classic_book.css")
    
    pdf_files = []
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            html_content = f.read()
            html_body = markdown.markdown(html_content, extensions=['tables', 'fenced_code'])
        
        # Generar HTML completo con footer
        html = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet" href="{css}">
            </head>
            <body>
                {html_body}
                <div class="footer"></div>
            </body>
        </html>
        """
        
        # Generar PDF con WeasyPrint
        pdf_path = output_dir / f"{md_file.stem}.pdf"
        HTML(string=html).write_pdf(
            pdf_path,
            stylesheets=[CSS(filename=css)]
        )
        pdf_files.append(pdf_path)
        print(f"✅ Convertido: {md_file} -> {pdf_path}")
    
    # Combinar PDFs si es necesario
    if merge or len(pdf_files) > 1:
        merger = PdfMerger()
        for pdf in pdf_files:
            merger.append(str(pdf))
        merged_path = output_dir / "merged.pdf"
        merger.write(str(merged_path))
        merger.close()
        print(f"\n📚 PDF combinado: {merged_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convierte Markdown a PDF")
    parser.add_argument("input", help="Archivo .md o directorio con archivos .md")
    parser.add_argument("-o", "--output", default="pdf_output", help="Directorio de salida")
    parser.add_argument("--css", help="Archivo CSS para estilos personalizados")
    parser.add_argument("--merge", action="store_true", help="Combinar todos los PDFs en uno")
    
    args = parser.parse_args()
    
    try:
        convert_md_to_pdf(args.input, args.output, args.css, args.merge)
        print("\n🎉 Conversión completada!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)