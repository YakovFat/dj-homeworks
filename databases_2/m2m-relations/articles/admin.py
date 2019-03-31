from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Relationship, Section


class SectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        print(self.forms)
        count = 0
        for form in self.forms:

            if form.cleaned_data and form.cleaned_data['main_sec']:
                count += 1
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        if count > 1:
            raise ValidationError('Основным может быть только один раздел')
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Укажите основной раздел')
            # raise ValidationError('Основной раздел может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода


class SectionInline(admin.TabularInline):
    model = Relationship
    formset = SectionInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
