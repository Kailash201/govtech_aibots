import io
from unstructured.partition.doc import partition_doc

from .fileModel import FileModel

class DOCModel(FileModel):
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def extract_text(self):
        file_content = io.BytesIO(self.content) 
        elements = partition_doc(file=file_content)
        extracted_text = ""
        for e in elements:
            extracted_text += e.text
        
        return extracted_text
    
    def get_extension(self):
        return ".doc"