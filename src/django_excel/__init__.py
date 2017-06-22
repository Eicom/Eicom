from django.core.files.uploadhandler import (
    MemoryFileUploadHandler, TemporaryFileUploadHandler)
from django.core.files.uploadedfile import (
    InMemoryUploadedFile, TemporaryUploadedFile)
from django.http import HttpResponse
import pyexcel as pe
import pyexcel_webio as webio
from ._compact import DJANGO_ONE_SIX
from pyexcel_webio import (
    make_response,
    make_response_from_array,
    make_response_from_dict,
    make_response_from_records,
    make_response_from_query_sets
)


class ExcelMixin(webio.ExcelInput):
    def get_params(self, **keywords):
        extension = self.name.split(".")[-1]
        keywords['file_type'] = extension
        content = self.file.read()
        if content:
            keywords['file_content'] = content
        else:
            raise IOError("No content was uploaded")
        return keywords

    def save_to_database(self, model=None, initializer=None, mapdict=None,
                         **keywords):
        params = self.get_params(**keywords)
        if 'name_columns_by_row' not in params:
            params['name_columns_by_row'] = 0
        if 'name_rows_by_column' not in params:
            params['name_rows_by_column'] = -1
        params['dest_model'] = model
        params['dest_initializer'] = initializer
        params['dest_mapdict'] = mapdict

    def save_book_to_database(self, models=None, initializers=None,
                              mapdicts=None, batch_size=None, **keywords):
        params = self.get_params(**keywords)
        params['dest_models'] = models
        params['dest_initializers'] = initializers
        params['dest_mapdicts'] = mapdicts
        params['dest_batch_size'] = batch_size
        pe.save_book_as(**params)


class ExcelInMemoryUploadedFile(ExcelMixin, InMemoryUploadedFile):
    pass


class TemporaryUploadedExcelFile(ExcelMixin, TemporaryUploadedFile):
    pass


class ExcelMemoryFileUploadHandler(MemoryFileUploadHandler):
    def file_complete(self, file_size):
        if not self.activated:
            return
        self.file.seek(0)
        keywords = dict(
            file=self.file,
            field_name=self.field_name,
            name=self.file_name,
            content_type=self.content_type,
            size=file_size,
            charset=self.charset
        )
        if not DJANGO_ONE_SIX:
            keywords["content_type_extra"] = self.content_type_extra
        return ExcelInMemoryUploadedFile(**keywords)


class TemporaryExcelFileUploadHandler(TemporaryFileUploadHandler):
    def new_file(self, file_name, *args, **kwargs):
        super(TemporaryFileUploadHandler, self).new_file(
            file_name,
            *args,
            **kwargs)
        custom_args = [
            self.file_name,
            self.content_type,
            0,
            self.charset]
        if not DJANGO_ONE_SIX:
            custom_args.append(self.content_type_extra)
        self.file = TemporaryUploadedExcelFile(*custom_args)


def _make_response(content, content_type, status, file_name=None):
    response = HttpResponse(content, content_type=content_type, status=status)
    if file_name:
        response["Content-Disposition"] = (
            "attachment; filename=%s" % (file_name))
    return response


webio.ExcelResponse = _make_response


def make_response_from_a_table(model, file_type, status=200, file_name=None,
                               **keywords):
    sheet = pe.get_sheet(model=model, **keywords)
    return make_response(sheet, file_type, status, file_name=file_name,
                         **keywords)


def make_response_from_tables(models, file_type, status=200, file_name=None,
                              **keywords):
    book = pe.get_book(models=models, **keywords)
    return make_response(book, file_type, status, file_name=file_name,
                         **keywords)
