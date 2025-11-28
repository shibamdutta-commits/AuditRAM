import os
import shutil
import subprocess
from pathlib import Path
from docx2pdf import convert as docx2pdf_convert

def has_libreoffice():
    return shutil.which("libreoffice") or shutil.which("soffice")

def try_docx2pdf(docx_path, out_dir):
    try:
        out_path = Path(out_dir) / (Path(docx_path).stem + ".pdf")
        docx2pdf_convert(docx_path, str(out_path))
        if out_path.exists():
            return str(out_path)
    except:
        pass
    return None

def try_libreoffice_convert(input_path, out_dir):
    try:
        cmd = ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", out_dir, input_path]
        if shutil.which("libreoffice") is None and shutil.which("soffice"):
            cmd[0] = "soffice"
        subprocess.run(cmd, check=True)
        out = Path(out_dir) / (Path(input_path).stem + ".pdf")
        if out.exists():
            return str(out)
    except:
        pass
    return None

def convert_to_pdf_if_needed(input_path, tmp_out_dir):
    p = Path(input_path)
    ext = p.suffix.lower()

    if ext == ".pdf":
        return str(input_path)

    if ext == ".docx":
        res = try_docx2pdf(input_path, tmp_out_dir)
        if res: return res
        if has_libreoffice():
            return try_libreoffice_convert(input_path, tmp_out_dir)
        return None

    if ext in [".xlsx", ".xls"]:
        if has_libreoffice():
            return try_libreoffice_convert(input_path, tmp_out_dir)
        return None

    return None
