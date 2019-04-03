import datetime
import os
import os.path
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        files = os.listdir(settings.FILES_PATH)
        data_return = {'files': []}
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        data_input = None
        if date is not None:
            data_input = datetime.datetime.strptime(date, '%Y-%m-%d')
        for file in files:
            file_info = os.stat(os.path.join(settings.FILES_PATH, file))
            if data_input is not None and datetime.datetime.utcfromtimestamp(
                    file_info.st_ctime).date() != data_input:
                continue
            data_return['files'].append({
                'name': file,
                'ctime': datetime.datetime.utcfromtimestamp(
                    file_info.st_ctime),
                'mtime': datetime.datetime.utcfromtimestamp(
                    file_info.st_mtime)
            })
        return data_return


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    path = os.path.join(settings.FILES_PATH, name)
    if os.path.exists(path):
        with open(str(path), encoding='utf8') as f:
            file = f.read()
    else:
        name = 'Not found'
        file = 'Not found'
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file}
    )
