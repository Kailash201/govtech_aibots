import io
from th_assign.filetypes.fileModel import FileModel
from unstructured.partition.ppt import partition_ppt

#NEED INSTALL LIBRE

class PPTModel(FileModel):
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def extract_text(self):
        file_content = io.BytesIO(self.content) 
        elements = partition_ppt(file=file_content)
        extracted_text = ""
        for e in elements:
            extracted_text += e.text
        
        return extracted_text
    
    def get_extension(self):
        return ".doc"