from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_pdf_path, output_folder, number_in_page):
    reader = PdfReader(input_pdf_path)

    total_pages = len(reader.pages)
    num_chunks = (total_pages + number_in_page - 1) // number_in_page

    for i in range(num_chunks):
        writer = PdfWriter()
        start_page = i * number_in_page
        end_page = min((i + 1) * number_in_page, total_pages)

        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])

        output_pdf_path = f"{output_folder}/output_{i + 1}.pdf"
        with open(output_pdf_path, "wb") as f:
            writer.write(f)



input_pdf = r"C:\Users\ASUS\Desktop\ICT November 2005.pdf"  # Change this to the path of your input PDF
output_folder = r"C:\Users\ASUS\Desktop\output"  # Change this to the desired output folder
number_in_page = 400  # Change this to the desired number of pages per output PDF

split_pdf(input_pdf, output_folder, number_in_page)


