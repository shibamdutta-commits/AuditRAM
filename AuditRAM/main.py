import os
import sys
import shutil
import tempfile
from pathlib import Path
from converter_helpers import convert_to_pdf_if_needed
from pdf_handler import highlight_in_pdf
from image_handler import highlight_in_image

SUPPORTED_IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".tiff", ".bmp"}

def ensure_output_dir():
    out = Path("output")
    out.mkdir(exist_ok=True)
    return out

def main():
    print("=== AuditRAM Highlighter (Full) ===")
    file_path = input("Enter path to your file (PDF / DOCX / XLSX / image): ").strip().strip('"')
    if not file_path:
        print("No file provided. Exiting.")
        return
    search_text = input("Enter text to search (case-insensitive): ").strip()
    if not search_text:
        print("No search text provided. Exiting.")
        return

    fp = Path(file_path)
    if not fp.exists():
        print(f"File not found: {file_path}")
        return

    out_dir = ensure_output_dir()

    if fp.suffix.lower() in SUPPORTED_IMAGE_EXTS:
        print("Processing image...")
        out_path = out_dir / f"{fp.stem}_highlighted{fp.suffix}"
        highlight_in_image(str(fp), search_text, str(out_path))
        print(f"Done. Output: {out_path}")
        return

    with tempfile.TemporaryDirectory() as tmp:
        converted = convert_to_pdf_if_needed(str(fp), tmp)
        if not converted:
            print("Conversion to PDF failed.")
            return

        converted_paths = converted if isinstance(converted, list) else [converted]
        outputs = []
        for pdf_path in converted_paths:
            pdfp = Path(pdf_path)
            out_pdf = out_dir / f"{pdfp.stem}_highlighted.pdf"
            print(f"Highlighting in: {pdfp.name}")
            ok = highlight_in_pdf(str(pdfp), search_text, str(out_pdf))
            if ok:
                outputs.append(str(out_pdf))
            else:
                print(f"Failed to highlight {pdfp}")

        print("Finished. Created outputs:")
        for o in outputs:
            print(" -", o)

if __name__ == "__main__":
    main()
