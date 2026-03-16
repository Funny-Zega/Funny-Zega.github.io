import sys
import pypdf

try:
    reader = pypdf.PdfReader(r"d:\Web\CV_Embedded_System_DongNguyenKhanhDuy.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    print(text)
except Exception as e:
    print(f"Error: {e}")
