import fitz

def highlight_in_pdf(pdf_path: str, search_text: str, output_path: str) -> bool:
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print("Failed to open PDF:", e)
        return False

    text_to_find = search_text.strip()
    if not text_to_find:
        print("Empty search string.")
        return False

    for page_number in range(doc.page_count):
        page = doc.load_page(page_number)
        rects = page.search_for(text_to_find)

        for r in rects:
            try:
                annot = page.add_rect_annot(r)
                annot.set_colors(stroke=(1, 0, 0))
                annot.set_border(width=1)
                annot.update()
            except Exception:
                pass

    try:
        doc.save(output_path)
    except Exception as e:
        print("Failed to save output PDF:", e)
        doc.close()
        return False
    doc.close()
    return True
