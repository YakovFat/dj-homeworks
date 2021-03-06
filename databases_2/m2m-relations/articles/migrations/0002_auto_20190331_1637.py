# Generated by Django 2.1.1 on 2019-03-31 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_sec', models.BooleanField(verbose_name='Соновной')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
            options={
                'verbose_name': 'Тематика статьи',
                'verbose_name_plural': 'Тематика статьи',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sections', models.CharField(max_length=50, verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Разделы',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.AddField(
            model_name='relationship',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Section'),
        ),
        migrations.AddField(
            model_name='article',
            name='sections',
            field=models.ManyToManyField(related_name='articles', through='articles.Relationship', to='articles.Section'),
        ),
    ]
