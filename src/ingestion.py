from pypdf import PdfReader
import os, glob

def extract_pdfs(file_path: str):
    read_files = glob.glob(os.path.join(file_path, "*.pdf"))
    output = []

    for file in read_files:
        try: 
            reader = PdfReader(file)
        except Exception as e:
            print(e)
            continue
        
        for i, page in enumerate(reader.pages):
            text = page.extract_text()

            if not text:
                continue

            text = text.strip()

            if len(text) < 10:
                continue

            output.append({
                "file": file,
                "page_num": i,
                "text": text
            })
    
    return output