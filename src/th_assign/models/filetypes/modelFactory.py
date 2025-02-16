from beanie import Document

from ..beanieModels import WebsiteDocument, FileDocument
from .websiteModel import WebsiteModel
from .pdfModel import PDFModel
from .docModel import DOCModel
from .docxModel import DOCXModel
from .pptModel import PPTModel
from .pptxModel import PPTXModel
from .xlsModel import XLSModel
from .xlsxModel import XLSXModel


class FileModelFactory:
    @staticmethod
    def create(obj: Document):
        if isinstance(obj, WebsiteDocument):
            return WebsiteModel(
                filename=obj.url,
                content=obj.url
            )
        elif isinstance(obj, FileDocument):
            if obj.content_type == ".pdf":
                return PDFModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == ".doc":
                return DOCModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == ".docx":
                return DOCXModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == ".ppt":
                return PPTModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == ".pptx":
                return PPTXModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == ".xls":
                return XLSModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == ".xlsx":
                return XLSXModel(
                    filename=obj.name,
                    content=obj.content
                )
            else:
                print("File type is no supported")
                return None
        else:
                print("File type is no supported")
                return None