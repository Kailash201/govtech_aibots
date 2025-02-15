from unstructured.partition.html import partition_html
from .fileModel import FileModel

class WebsiteModel(FileModel):
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def extract_text(self):
        elements = partition_html(url=self.content)
        extracted_text = ""
        for e in elements:
            extracted_text += e.text
        
        return extracted_text
    
    def get_extension(self):
        return ".html"