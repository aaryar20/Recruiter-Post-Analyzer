import pdfplumber


def read_file(uploaded_file):
    """
    Read uploaded TXT or PDF files and return extracted text.
    """

    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    elif uploaded_file.name.endswith(".pdf"):

        text = ""

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    return ""