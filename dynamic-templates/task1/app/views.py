import csv
from django.shortcuts import render
from django.views.generic import TemplateView


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        context = {}
        with open('inflation_russia.csv', encoding='utf-8', newline='') as f:
            read = csv.reader(f, delimiter=';')
            list_csv = [i for i in read]
            first_column = list_csv.pop(0)
        list_info = []
        list_1 = []
        for lis in list_csv:
            for i in lis:
                if '.' in i:
                    list_1.append(float(i))
                elif i.isdigit():
                    list_1.append(int(i))
                elif len(i) == 0:
                    list_1.append('-')
            list_info.append(list_1)
            list_1 = []
        print(list_info)
        context['first_column'] = first_column
        context['info'] = list_info
        return render(request, self.template_name,
                      context)
