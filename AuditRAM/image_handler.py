import cv2
import pytesseract

def highlight_in_image(image_path: str, search_text: str, output_path: str) -> bool:
    img = cv2.imread(image_path)
    if img is None:
        print("Failed to open image:", image_path)
        return False

    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    texts = data['text']
    search = search_text.lower()

    for i, word in enumerate(texts):
        if word.lower() == search:
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)

    cv2.imwrite(output_path, img)
    return True
