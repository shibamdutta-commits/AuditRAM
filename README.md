Features:
- Supports PDF, DOCX, XLSX, JPG, PNG, TIFF
- Case-insensitive text search
- Red bounding-box annotation
- PDF highlighting using PyMuPDF
- Image text detection using Tesseract OCR + OpenCV
- DOCX/XLSX → PDF conversion (docx2pdf or LibreOffice)
- Clean output naming: filename_highlighted.pdf

Folder Structure:
AuditRAM/
main.py
pdf_handler.py
image_handler.py
converter_helpers.py
requirements.txt
README.md
invoice.pdf
output/

Installation:
pip install -r requirements.txt

Or install packages manually:
pip install pymupdf
pip install python-docx
pip install openpyxl
pip install pytesseract
pip install opencv-python
pip install Pillow
pip install docx2pdf

Install Tesseract OCR from:
https://github.com/UB-Mannheim/tesseract/wiki

How to Run:
python main.py

Example:
Enter path to your file: invoice.pdf
Enter text to search: Invoice

Output saved in: output/filename_highlighted.pdf

How It Works:
PDF: PyMuPDF searches for text and draws annotation boxes.
DOCX/XLSX: Converted to PDF first, then processed.
Images: Tesseract OCR extracts text; OpenCV draws rectangles.

Purpose:
This project was developed as part of the AuditRAM technical assignment.
