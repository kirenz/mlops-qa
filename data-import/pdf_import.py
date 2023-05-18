"""
Import PDF
"""

import os
import pdfplumber


def extract_text_from_pdf(file_path):
    """
    Function to extract text from pdf file using PDFPlumber.
    """
    text = ''
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def extract_text_from_txt(file_path):
    """
    Function to extract text from text file using built-in open function.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def extract_text(file_path):
    """
    Function to extract text from file.
    Detects file type and uses the appropriate function to extract text.
    """
    _, file_extension = os.path.splitext(file_path)

    if file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension == '.txt':
        return extract_text_from_txt(file_path)
    else:
        print(f"Unsupported file type: {file_extension}")
        return None
