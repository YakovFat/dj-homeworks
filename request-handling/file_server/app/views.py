import datetime
import os

from django.shortcuts import render
from django.views.generic import TemplateView
from app.settings import FILES_PATH


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        files = os.listdir(FILES_PATH)
        data_return = {'files': []}
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        if date is None:
            for file in files:
                file_info = os.stat(os.path.join(FILES_PATH, file))
                data_return['files'].append({
                    'name': file,
                    'ctime': datetime.datetime.utcfromtimestamp(
                        file_info.st_ctime),
                    'mtime': datetime.datetime.utcfromtimestamp(
                        file_info.st_mtime)
                })
            return data_return
        else:
            date = date.split('-')
            data_input = datetime.datetime(int(date[0]), int(date[1]),
                                           int(date[2])).date()
            for file in files:
                file_info = os.stat(os.path.join(FILES_PATH, file))

                if datetime.datetime.utcfromtimestamp(
                        file_info.st_ctime).date() == data_input:
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
    path = os.path.join(FILES_PATH, name)
    with open(str(path), encoding='utf8') as f:
        file = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': 'file_name_1.txt', 'file_content': file}
    )
