# Generated by Django 2.1.2 on 2022-12-07 03:10

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20221130_0249'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to=common.models.get_file_path)),
            ],
        ),
    ]