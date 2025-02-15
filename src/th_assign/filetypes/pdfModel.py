import io
from th_assign.filetypes.fileModel import FileModel
from unstructured.partition.pdf import partition_pdf


class PDFModel(FileModel):
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def extract_text(self):
        file_content = io.BytesIO(self.content) 
        elements = partition_pdf(
            file=file_content,
            strategy="hi_res",                                     
            )
        extracted_text = ""
        for e in elements:
            extracted_text += e.text
        
        return extracted_text
    
    def get_extension(self):
        return ".pdf"
