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
            if obj.content_type == "application/pdf":
                return PDFModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == "application/msword":
                return DOCModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                return DOCXModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == "application/vnd.ms-powerpoint":
                return PPTModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == "application/vnd.openxmlformats-officedocument.presentationml.presentation":
                return PPTXModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == "application/vnd.ms-excel":
                return XLSModel(
                    filename=obj.name,
                    content=obj.content
                )
            elif obj.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
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