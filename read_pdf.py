import sys
try:
    import fitz  # PyMuPDF
    doc = fitz.open(sys.argv[1])
    for page in doc:
        print(page.get_text())
except ImportError:
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(sys.argv[1])
        for page in reader.pages:
            print(page.extract_text())
    except ImportError:
        print("No suitable PDF library found.")
