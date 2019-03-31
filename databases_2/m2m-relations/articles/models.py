from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    sections = models.ManyToManyField('Section', related_name='articles', through='Relationship')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Section(models.Model):
    sections = models.CharField(max_length=50, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Разделы'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.sections


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    main_sec = models.BooleanField(verbose_name='Соновной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'