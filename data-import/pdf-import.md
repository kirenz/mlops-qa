# PDF import

extract_text_from_pdf(file_path): 

This function takes a PDF file path as input and uses the pdfplumber.open() function to open the PDF file. It then loops over each page in the PDF and extracts the text using the page.

extract_text() function.

The extracted text from all pages is concatenated and returned.

extract_text_from_txt(file_path): This function takes a text file path as input and uses the built-in open() function to open the text file in read mode. It then reads the entire file as a string using the file.read() function and returns this string.

extract_text(file_path): This function is the main entry point for text extraction. It takes a file path as input, determines the file type by checking the file extension, and then calls the appropriate function to extract the text. If the file type is not supported, it prints an error message and returns None.

Please install the necessary Python libraries (if you haven't done so already) by running pip install pdfplumber. This script currently only supports PDF and text files, but it could be easily extended to support other file types by adding additional functions similar to extract_text_from_pdf() and extract_text_from_txt().