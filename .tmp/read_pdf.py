import pdfplumber

with pdfplumber.open('Todo_Directo_2_Paginas_Sales_Cheat_Sheet_ES.pdf') as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"\n{'='*80}")
        print(f"PAGE {i+1}")
        print(f"{'='*80}")
        text = page.extract_text()
        if text:
            print(text)
        tables = page.extract_tables()
        if tables:
            for j, table in enumerate(tables):
                print(f"\n--- Table {j+1} ---")
                for row in table:
                    print(row)
