from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from _compact import JsonResponse
from django import forms
import django_excel as excel
from .models import Producto, Question, Choice

data = [
    [1, 2, 3,
     4, 5, 6,
     7, 8, 9]
]


class UploadFileForm(forms.Form):
    file = forms.FileField()


@login_required
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
        else:
            form = UploadFileForm()
        return render(
            request,
            'upload_form.html',
            {
                'form': form,
                'title': 'Excel file upload and download example',
                'header': ('Please choose any excel file ' +
                           'from your cloned repository:')
            })


@login_required
def download(request, file_type):
    sheet = excel.pe.Sheet(data)
    return excel.make_response(sheet, file_type)


@login_required
def download_as_attachment(request, file_type, file_name):
    return excel.make_response_from_array(data, file_type, file_name=file_name)


@login_required
def export_data(request, atype):
    if atype == "sheet":
        return excel.make_response_from_a_table(Producto, 'xls',
                                                file_name="sheet")
    elif atype == "book":
        return excel.make_response_from_tables([Question, Choice], 'xls',
                                               file_name="book")
    elif atype == "custom":
        question = Question.objects.get(slug='ide')
        query_sets = Choice.objects.filter(question=question)
        column_names = ['choice_text', 'id', 'votes']
        return excel.make_response_from_query_sets(
            query_sets,
            column_names,
            'xls',
            file_name="custom"
        )
    else:
        return HttpResponseBadRequest(
            "Bad request. please put one of these " +
            "in your url suffix: sheet, book or custom")


@login_required
def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        def choice_func(row):
            q = Producto.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Producto],
                initializers=[None, choice_func],
                mapdicts=[
                    ['clave', 'descripcion', 'unidad',
                     'marca', 'modelo', 'linea',
                     'familia', 'divisa', 'precio_pub']]
            )
            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Ploease upload sample-data.xls:'
        })


@login_required
def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=9,
                model=Producto,
                mapdict=['clave', 'descripcion', 'unidad',
                         'marca', 'modelo', 'linea',
                         'familia', 'divisa', 'precio_pub'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})


@login_required
def exchange(request, file_type):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        filehandle = request.FILES['file']
        return excel.make_response(filehandle.get_sheet(), file_type)
    else:
        return HttpResponseBadRequest()


@login_required
def parse(request, data_struct_type):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        filehandle = request.FILES['file']
        if data_struct_type == "array":
            return JsonResponse({"result": filehandle.get_array()})
        elif data_struct_type == "dict":
            return JsonResponse(filehandle.get_dict())
        elif data_struct_type == "records":
            return JsonResponse({"result": filehandle.get_records()})
        elif data_struct_type == "book":
            return JsonResponse(filehandle.get_book().to_dict())
        elif data_struct_type == "book_dict":
            return JsonResponse(filehandle.get_book_dict())
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
