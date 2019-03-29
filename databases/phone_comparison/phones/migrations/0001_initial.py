# Generated by Django 2.1.1 on 2019-03-25 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('os', models.TextField()),
                ('screen_resolution', models.TextField()),
                ('ram', models.FloatField()),
                ('weight', models.FloatField()),
                ('nfc', models.BooleanField()),
                ('color', models.TextField()),
                ('battery', models.FloatField()),
                ('dual_camera', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='phones.Phone')),
                ('face_id', models.BooleanField()),
            ],
            bases=('phones.phone',),
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='phones.Phone')),
                ('borderless_screen', models.BooleanField()),
            ],
            bases=('phones.phone',),
        ),
    ]